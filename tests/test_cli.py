import contextlib
import io
import json
import runpy
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

from cheeku_infinity.catalog import PROJECT_BY_ID, PROJECTS
from cheeku_infinity.cli import (
    cmd_clone_one,
    local_project_state,
    main,
    run,
    validate_update_checkout,
)


class CliTests(unittest.TestCase):
    def run_cli(self, args):
        out, err = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            code = main(args)
        return code, out.getvalue(), err.getvalue()

    def test_list_json(self):
        code, output, _ = self.run_cli(["list", "--json"])
        self.assertEqual(code, 0)
        self.assertEqual(len(json.loads(output)), 16)

    def test_kind_and_domain_filters(self):
        code, output, _ = self.run_cli(["list", "--kind", "application"])
        self.assertEqual(code, 0)
        self.assertIn("affine", output)
        self.assertIn("autoclip", output)
        self.assertNotIn("firecrawl", output)

        code, output, _ = self.run_cli(["list", "--domain", "research"])
        self.assertEqual(code, 0)
        self.assertIn("firecrawl", output)
        self.assertIn("last30days-skill", output)

    def test_list_with_no_matches(self):
        code, output, _ = self.run_cli(["list", "--domain", "not-a-real-domain"])
        self.assertEqual(code, 0)
        self.assertIn("0 projects", output)

    def test_info_project_and_unknown_project(self):
        code, output, _ = self.run_cli(["info", "superpowers"])
        self.assertEqual(code, 0)
        self.assertIn("Software Engineering", output)
        self.assertIn("https://github.com/obra/superpowers", output)

        code, _, error = self.run_cli(["info", "missing"])
        self.assertEqual(code, 2)
        self.assertIn("Unknown project ID", error)

    def test_invalid_clone_arguments(self):
        with patch("cheeku_infinity.cli.shutil.which", return_value="/usr/bin/git"):
            code, _, error = self.run_cli(["clone"])
            self.assertEqual(code, 2)
            self.assertIn("Choose a project ID", error)

            code, _, error = self.run_cli(["clone", "unknown"])
            self.assertEqual(code, 2)
            self.assertIn("Unknown project ID", error)

            code, _, error = self.run_cli(["clone", "superpowers", "--all"])
            self.assertEqual(code, 2)
            self.assertIn("either a project ID or --all", error)

    def test_clone_requires_git(self):
        with patch("cheeku_infinity.cli.shutil.which", return_value=None):
            code, _, error = self.run_cli(["clone", "superpowers"])
        self.assertEqual(code, 127)
        self.assertIn("Git is required", error)

    def test_clone_all_collects_failures(self):
        with tempfile.TemporaryDirectory() as folder:
            with (
                patch("cheeku_infinity.cli.shutil.which", return_value="/usr/bin/git"),
                patch("cheeku_infinity.cli.cmd_clone_one", side_effect=[0] + [2] * 15),
            ):
                code, _, error = self.run_cli(["clone", "--all", "--destination", folder])
        self.assertEqual(code, 1)
        self.assertIn("Could not clone", error)

    def test_clone_one_handles_existing_directory_states(self):
        project = PROJECT_BY_ID["superpowers"]
        with tempfile.TemporaryDirectory() as folder:
            destination = Path(folder)
            target = destination / project["id"]
            target.mkdir()
            (target / ".git").mkdir()
            with contextlib.redirect_stdout(io.StringIO()) as output:
                self.assertEqual(cmd_clone_one(project, destination), 0)
            self.assertIn("Already cloned", output.getvalue())

        with tempfile.TemporaryDirectory() as folder:
            destination = Path(folder)
            (destination / project["id"]).mkdir()
            with contextlib.redirect_stderr(io.StringIO()) as error:
                self.assertEqual(cmd_clone_one(project, destination), 2)
            self.assertIn("Refusing to overwrite", error.getvalue())

    def test_clone_one_invokes_git_for_new_project(self):
        project = PROJECT_BY_ID["superpowers"]
        with tempfile.TemporaryDirectory() as folder:
            with patch("cheeku_infinity.cli.run", return_value=0) as mocked_run:
                self.assertEqual(cmd_clone_one(project, Path(folder)), 0)
        self.assertEqual(mocked_run.call_count, 1)
        self.assertEqual(mocked_run.call_args.args[0][0:2], ["git", "clone"])

    def test_update_validation_and_missing_clone(self):
        with patch("cheeku_infinity.cli.shutil.which", return_value=None):
            code, _, _ = self.run_cli(["update", "superpowers"])
        self.assertEqual(code, 127)

        with patch("cheeku_infinity.cli.shutil.which", return_value="/usr/bin/git"):
            code, _, error = self.run_cli(["update"])
            self.assertEqual(code, 2)
            self.assertIn("Choose a project ID", error)

            code, _, error = self.run_cli(["update", "unknown"])
            self.assertEqual(code, 2)
            self.assertIn("Unknown project ID", error)

        with patch("cheeku_infinity.cli.shutil.which", return_value="/usr/bin/git"):
            code, _, error = self.run_cli(["update", "superpowers"])
        self.assertEqual(code, 1)
        self.assertIn("Not cloned", error)

    def test_update_all_fast_forward_success_and_failure(self):
        project = PROJECT_BY_ID["superpowers"]
        with tempfile.TemporaryDirectory() as folder:
            (Path(folder) / project["id"] / ".git").mkdir(parents=True)
            with (
                patch("cheeku_infinity.cli.shutil.which", return_value="/usr/bin/git"),
                patch("cheeku_infinity.cli.run", return_value=0) as mocked_run,
                patch("cheeku_infinity.cli.validate_update_checkout", return_value=None),
            ):
                code, _, _ = self.run_cli(["update", "--all", "--destination", folder])
            self.assertEqual(code, 0)
            mocked_run.assert_called_once()

        with tempfile.TemporaryDirectory() as folder:
            (Path(folder) / project["id"] / ".git").mkdir(parents=True)
            with (
                patch("cheeku_infinity.cli.shutil.which", return_value="/usr/bin/git"),
                patch("cheeku_infinity.cli.run", return_value=1),
                patch("cheeku_infinity.cli.validate_update_checkout", return_value=None),
            ):
                code, _, error = self.run_cli(["update", "--all", "--destination", folder])
            self.assertEqual(code, 1)
            self.assertIn("Update failed or skipped", error)

    def test_run_reports_missing_executable(self):
        with patch("cheeku_infinity.cli.subprocess.run", side_effect=FileNotFoundError):
            with contextlib.redirect_stderr(io.StringIO()) as error:
                result = run(["missing-command"])
        self.assertEqual(result, 127)
        self.assertIn("Required command not found", error.getvalue())

    def test_status_json_on_empty_destination(self):
        with tempfile.TemporaryDirectory() as folder:
            code, output, _ = self.run_cli(["status", "--destination", folder, "--json"])
        self.assertEqual(code, 0)
        statuses = json.loads(output)
        self.assertEqual(len(statuses), 16)
        self.assertTrue(all(not row["cloned"] for row in statuses))

    def test_local_project_state_clean_and_dirty(self):
        project = PROJECT_BY_ID["superpowers"]
        with tempfile.TemporaryDirectory() as folder:
            target = Path(folder) / project["id"]
            (target / ".git").mkdir(parents=True)
            (target / "LICENSE").write_text("MIT", encoding="utf-8")
            results = [
                SimpleNamespace(returncode=0, stdout="main\n"),
                SimpleNamespace(returncode=0, stdout=""),
            ]
            with patch("cheeku_infinity.cli.subprocess.run", side_effect=results):
                state = local_project_state(project, Path(folder))
        self.assertTrue(state["cloned"])
        self.assertFalse(state["dirty"])
        self.assertEqual(state["branch"], "main")
        self.assertIn("LICENSE", state["license_files"])

        with tempfile.TemporaryDirectory() as folder:
            (Path(folder) / project["id"] / ".git").mkdir(parents=True)
            results = [
                SimpleNamespace(returncode=1, stdout=""),
                SimpleNamespace(returncode=0, stdout=" M README.md"),
            ]
            with patch("cheeku_infinity.cli.subprocess.run", side_effect=results):
                state = local_project_state(project, Path(folder))
        self.assertTrue(state["dirty"])
        self.assertIsNone(state["branch"])

    def test_update_all_skips_uncloned_projects(self):
        with tempfile.TemporaryDirectory() as folder:
            with patch("cheeku_infinity.cli.shutil.which", return_value="/usr/bin/git"):
                code, output, _ = self.run_cli(["update", "--all", "--destination", folder])
        self.assertEqual(code, 0)
        self.assertIn("No cloned repositories to update", output)

    def test_audit_on_empty_destination_and_missing_license(self):
        with tempfile.TemporaryDirectory() as folder:
            code, output, _ = self.run_cli(["audit", "--destination", folder])
        self.assertEqual(code, 0)
        self.assertIn("No source repositories cloned", output)

        project = PROJECT_BY_ID["superpowers"]
        with tempfile.TemporaryDirectory() as folder:
            (Path(folder) / project["id"] / ".git").mkdir(parents=True)
            with (
                patch("cheeku_infinity.cli.subprocess.run", side_effect=[
                    SimpleNamespace(returncode=0, stdout="main"),
                    SimpleNamespace(returncode=0, stdout=" M README.md"),
                ]),
                contextlib.redirect_stdout(io.StringIO()) as output,
            ):
                code = main(["audit", "--destination", folder])
        self.assertEqual(code, 0)
        self.assertIn("NO COMMON LICENSE", output.getvalue())
        self.assertIn("Local modifications detected", output.getvalue())

    def test_clone_single_project_success(self):
        with tempfile.TemporaryDirectory() as folder:
            with (
                patch("cheeku_infinity.cli.shutil.which", return_value="/usr/bin/git"),
                patch("cheeku_infinity.cli.cmd_clone_one", return_value=0) as mocked,
            ):
                code, output, _ = self.run_cli([
                    "clone", "superpowers", "--destination", folder
                ])
        self.assertEqual(code, 0)
        self.assertIn("Done. Review each upstream README", output)
        mocked.assert_called_once()

    def test_update_rejects_mixed_project_and_all_options(self):
        with patch("cheeku_infinity.cli.shutil.which", return_value="/usr/bin/git"):
            code, _, error = self.run_cli(["update", "superpowers", "--all"])
        self.assertEqual(code, 2)
        self.assertIn("either a project ID or --all", error)

    def test_status_human_readable_output_for_clean_and_dirty_repositories(self):
        states = [
            {
                "id": project["id"],
                "cloned": False,
                "dirty": None,
                "branch": None,
            }
            for project in PROJECTS
        ]
        states[0] = {
            "id": PROJECTS[0]["id"],
            "cloned": False,
            "dirty": None,
            "branch": None,
        }
        states[1] = {
            "id": PROJECTS[1]["id"],
            "cloned": True,
            "dirty": False,
            "branch": "main",
        }
        states[2] = {
            "id": PROJECTS[2]["id"],
            "cloned": True,
            "dirty": True,
            "branch": None,
        }
        with patch(
            "cheeku_infinity.cli.local_project_state", side_effect=states
        ):
            code, output, _ = self.run_cli(["status"])
        self.assertEqual(code, 0)
        self.assertIn("[--]", output)
        self.assertIn("[OK]", output)
        self.assertIn("[DIRTY]", output)
        self.assertIn("branch=unknown", output)
        self.assertIn("2/16 projects cloned.", output)

    def test_module_entrypoint_exits_after_version_output(self):
        with (
            patch("sys.argv", ["cheeku-infinity", "--version"]),
            contextlib.redirect_stdout(io.StringIO()) as output,
        ):
            with self.assertRaises(SystemExit) as error:
                runpy.run_module("cheeku_infinity.cli", run_name="__main__")
        self.assertEqual(error.exception.code, 0)
        self.assertIn("CHEEKU INFINITY", output.getvalue())

    def test_doctor_reports_current_environment(self):
        with patch("cheeku_infinity.cli.shutil.which", return_value="/usr/bin/git"):
            code, output, _ = self.run_cli(["doctor"])
        self.assertEqual(code, 0)
        self.assertIn("CHEEKU INFINITY doctor", output)
        self.assertIn(f"{len(PROJECTS)} entries", output)

    def test_doctor_returns_failure_when_prerequisites_are_missing(self):
        with (
            patch("cheeku_infinity.cli.sys.version_info", (3, 9, 0)),
            patch("cheeku_infinity.cli.shutil.which", return_value=None),
            patch("cheeku_infinity.cli.PROJECTS", []),
        ):
            code, output, _ = self.run_cli(["doctor"])
        self.assertEqual(code, 1)
        self.assertIn("[MISSING]", output)


    def test_update_guard_accepts_expected_clean_https_checkout(self):
        project = PROJECT_BY_ID["superpowers"]
        results = [
            SimpleNamespace(returncode=0, stdout="https://github.com/obra/superpowers.git\n"),
            SimpleNamespace(returncode=0, stdout="main\n"),
            SimpleNamespace(returncode=0, stdout=""),
        ]
        with patch("cheeku_infinity.cli.subprocess.run", side_effect=results):
            self.assertIsNone(validate_update_checkout(project, Path("/tmp/superpowers")))

    def test_update_guard_accepts_expected_clean_ssh_checkout(self):
        project = PROJECT_BY_ID["superpowers"]
        results = [
            SimpleNamespace(returncode=0, stdout="git@github.com:obra/superpowers.git\n"),
            SimpleNamespace(returncode=0, stdout="main\n"),
            SimpleNamespace(returncode=0, stdout=""),
        ]
        with patch("cheeku_infinity.cli.subprocess.run", side_effect=results):
            self.assertIsNone(validate_update_checkout(project, Path("/tmp/superpowers")))

    def test_update_guard_rejects_unexpected_origin(self):
        project = PROJECT_BY_ID["superpowers"]
        results = [SimpleNamespace(returncode=0, stdout="https://github.com/someone/else.git\n")]
        with patch("cheeku_infinity.cli.subprocess.run", side_effect=results):
            message = validate_update_checkout(project, Path("/tmp/superpowers"))
        self.assertIn("does not match", message)

    def test_update_guard_rejects_wrong_branch(self):
        project = PROJECT_BY_ID["superpowers"]
        results = [
            SimpleNamespace(returncode=0, stdout="https://github.com/obra/superpowers.git\n"),
            SimpleNamespace(returncode=0, stdout="feature/local-work\n"),
        ]
        with patch("cheeku_infinity.cli.subprocess.run", side_effect=results):
            message = validate_update_checkout(project, Path("/tmp/superpowers"))
        self.assertIn("expected 'main'", message)

    def test_update_guard_rejects_uncommitted_changes(self):
        project = PROJECT_BY_ID["superpowers"]
        results = [
            SimpleNamespace(returncode=0, stdout="https://github.com/obra/superpowers.git\n"),
            SimpleNamespace(returncode=0, stdout="main\n"),
            SimpleNamespace(returncode=0, stdout=" M README.md\n"),
        ]
        with patch("cheeku_infinity.cli.subprocess.run", side_effect=results):
            message = validate_update_checkout(project, Path("/tmp/superpowers"))
        self.assertIn("local changes are present", message)



if __name__ == "__main__":
    unittest.main()
