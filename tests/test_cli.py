import contextlib
import io
import json
import tempfile
import unittest

from cheeku_infinity.cli import main


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

    def test_kind_filter(self):
        code, output, _ = self.run_cli(["list", "--kind", "application"])
        self.assertEqual(code, 0)
        self.assertIn("affine", output)
        self.assertIn("autoclip", output)
        self.assertNotIn("firecrawl", output)

    def test_domain_filter(self):
        code, output, _ = self.run_cli(["list", "--domain", "research"])
        self.assertEqual(code, 0)
        self.assertIn("firecrawl", output)
        self.assertIn("last30days-skill", output)

    def test_info_project(self):
        code, output, _ = self.run_cli(["info", "superpowers"])
        self.assertEqual(code, 0)
        self.assertIn("Software Engineering", output)
        self.assertIn("https://github.com/obra/superpowers", output)

    def test_unknown_project(self):
        code, _, error = self.run_cli(["info", "missing"])
        self.assertEqual(code, 2)
        self.assertIn("Unknown project ID", error)

    def test_invalid_clone_arguments(self):
        code, _, error = self.run_cli(["clone"])
        self.assertEqual(code, 2)
        self.assertIn("Choose a project ID", error)

    def test_status_json_on_empty_destination(self):
        with tempfile.TemporaryDirectory() as folder:
            code, output, _ = self.run_cli(["status", "--destination", folder, "--json"])
        self.assertEqual(code, 0)
        statuses = json.loads(output)
        self.assertEqual(len(statuses), 16)
        self.assertTrue(all(not row["cloned"] for row in statuses))

    def test_update_all_skips_uncloned_projects(self):
        from unittest.mock import patch
        with tempfile.TemporaryDirectory() as folder:
            with patch("cheeku_infinity.cli.shutil.which", return_value="/usr/bin/git"):
                code, output, _ = self.run_cli(["update", "--all", "--destination", folder])
        self.assertEqual(code, 0)
        self.assertIn("No cloned repositories to update", output)

    def test_audit_on_empty_destination(self):
        with tempfile.TemporaryDirectory() as folder:
            code, output, _ = self.run_cli(["audit", "--destination", folder])
        self.assertEqual(code, 0)
        self.assertIn("No source repositories cloned", output)


if __name__ == "__main__":
    unittest.main()
