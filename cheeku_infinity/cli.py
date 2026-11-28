"""Command-line interface for the CHEEKU INFINITY source manager."""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path
from urllib.parse import urlparse

from . import __version__
from .catalog import PROJECTS, PROJECT_BY_ID

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DESTINATION = ROOT / "sources"
LICENSE_NAMES = (
    "LICENSE", "LICENSE.md", "LICENSE.txt", "COPYING", "COPYING.md",
    "NOTICE", "NOTICE.md", "THIRD_PARTY_NOTICES.md",
)


def run(command: list[str], cwd: Path | None = None) -> int:
    try:
        return subprocess.run(command, cwd=cwd, check=False).returncode
    except FileNotFoundError:
        print(f"Required command not found: {command[0]}", file=sys.stderr)
        return 127


def project_dir(project_id: str, destination: Path) -> Path:
    return destination.expanduser().resolve() / project_id


def print_project(project: dict) -> None:
    print(f"{project['name']} ({project['id']})")
    print(f"  Type:        {project['kind']}")
    print(f"  Domain:      {project['domain']}")
    print(f"  Repository:  {project['repository']}")
    print(f"  Upstream:    {project['url']}")
    print(f"  Branch:      {project['branch']}")
    print(f"  Description: {project['description']}")
    print(f"  Setup:       {project['setup']}")


def cmd_list(args: argparse.Namespace) -> int:
    projects = PROJECTS
    if args.kind:
        projects = [p for p in projects if p["kind"] == args.kind]
    if args.domain:
        query = args.domain.casefold()
        projects = [p for p in projects if query in p["domain"].casefold()]
    if args.json:
        print(json.dumps(projects, indent=2))
        return 0
    print(f"CHEEKU INFINITY v{__version__} — {len(projects)} projects\n")
    print(f"{'ID':<23} {'TYPE':<14} {'DOMAIN':<31} PROJECT")
    print("-" * 100)
    for p in projects:
        print(f"{p['id']:<23} {p['kind']:<14} {p['domain']:<31} {p['name']}")
    print("\nUse cheeku-infinity info <id> for details.")
    return 0


def cmd_info(args: argparse.Namespace) -> int:
    project = PROJECT_BY_ID.get(args.project)
    if not project:
        print(f"Unknown project ID: {args.project}", file=sys.stderr)
        print("Run cheeku-infinity list to see project IDs.", file=sys.stderr)
        return 2
    print_project(project)
    return 0


def cmd_clone_one(project: dict, destination: Path) -> int:
    target = project_dir(project["id"], destination)
    if target.exists():
        if (target / ".git").is_dir():
            print(f"Already cloned: {project['id']} ({target})")
            return 0
        print(f"Refusing to overwrite a non-Git directory: {target}", file=sys.stderr)
        return 2
    target.parent.mkdir(parents=True, exist_ok=True)
    print(f"Cloning {project['name']} -> {target}")
    return run([
        "git", "clone", "--depth", "1", "--branch", project["branch"],
        project["url"], str(target)
    ])


def cmd_clone(args: argparse.Namespace) -> int:
    if not shutil.which("git"):
        print("Git is required. Install Git first.", file=sys.stderr)
        return 127
    if args.all and args.project:
        print("Use either a project ID or --all, not both.", file=sys.stderr)
        return 2
    if args.all:
        selected = PROJECTS
    elif args.project in PROJECT_BY_ID:
        selected = [PROJECT_BY_ID[args.project]]
    elif args.project:
        print(f"Unknown project ID: {args.project}", file=sys.stderr)
        return 2
    else:
        print("Choose a project ID or pass --all.", file=sys.stderr)
        return 2

    failures = []
    for project in selected:
        code = cmd_clone_one(project, Path(args.destination))
        if code != 0:
            failures.append(project["id"])
    if failures:
        print("Could not clone: " + ", ".join(failures), file=sys.stderr)
        return 1
    print("Done. Review each upstream README and license before use.")
    return 0


def _repository_from_remote(remote_url: str) -> str | None:
    """Return owner/repository for a public GitHub remote URL."""
    value = remote_url.strip()
    if value.startswith("git@github.com:"):
        path = value.split(":", 1)[1]
    else:
        parsed = urlparse(value)
        if parsed.hostname != "github.com":
            return None
        path = parsed.path.lstrip("/")
    return path.removesuffix(".git").strip("/").casefold()


def validate_update_checkout(project: dict, target: Path) -> str | None:
    """Refuse updates when the checkout is not the expected clean upstream."""
    try:
        remote = subprocess.run(
            ["git", "remote", "get-url", "origin"], cwd=target,
            capture_output=True, text=True, check=False
        )
        if remote.returncode != 0:
            return "the origin remote could not be read"
        if _repository_from_remote(remote.stdout) != project["repository"].casefold():
            return "the origin remote does not match the catalogue repository"

        branch = subprocess.run(
            ["git", "branch", "--show-current"], cwd=target,
            capture_output=True, text=True, check=False
        )
        if branch.returncode != 0:
            return "the current branch could not be determined"
        if branch.stdout.strip() != project["branch"]:
            return (
                f"the checkout is on branch {branch.stdout.strip() or '<detached>'!r}; "
                f"expected {project['branch']!r}"
            )

        status = subprocess.run(
            ["git", "status", "--porcelain"], cwd=target,
            capture_output=True, text=True, check=False
        )
        if status.returncode != 0:
            return "the working-tree status could not be determined"
        if status.stdout.strip():
            return "local changes are present; commit or stash them before updating"
    except FileNotFoundError:
        return "Git is unavailable"

    return None


def cmd_update(args: argparse.Namespace) -> int:
    if not shutil.which("git"):
        print("Git is required. Install Git first.", file=sys.stderr)
        return 127
    if args.all and args.project:
        print("Use either a project ID or --all, not both.", file=sys.stderr)
        return 2
    if args.all:
        destination = Path(args.destination)
        selected = [
            project for project in PROJECTS
            if (project_dir(project["id"], destination) / ".git").is_dir()
        ]
        if not selected:
            print("No cloned repositories to update.")
            return 0
    elif args.project in PROJECT_BY_ID:
        selected = [PROJECT_BY_ID[args.project]]
    elif args.project:
        print(f"Unknown project ID: {args.project}", file=sys.stderr)
        return 2
    else:
        print("Choose a project ID or pass --all.", file=sys.stderr)
        return 2

    failures = []
    for project in selected:
        target = project_dir(project["id"], Path(args.destination))
        if not (target / ".git").is_dir():
            print(f"Not cloned: {project['id']} ({target})", file=sys.stderr)
            failures.append(project["id"])
            continue
        problem = validate_update_checkout(project, target)
        if problem:
            print(
                f"Refusing update for {project['id']}: {problem}.",
                file=sys.stderr
            )
            failures.append(project["id"])
            continue
        print(f"Updating {project['id']} (fast-forward only)")
        if run(
            ["git", "pull", "--ff-only", "origin", project["branch"]],
            cwd=target
        ) != 0:
            failures.append(project["id"])
    if failures:
        print("Update failed or skipped: " + ", ".join(failures), file=sys.stderr)
        return 1
    return 0


def local_project_state(project: dict, destination: Path) -> dict:
    target = project_dir(project["id"], destination)
    cloned = (target / ".git").is_dir()
    if not cloned:
        return {"id": project["id"], "name": project["name"], "cloned": False,
                "path": str(target), "branch": None, "dirty": None, "license_files": []}
    branch = subprocess.run(
        ["git", "branch", "--show-current"], cwd=target,
        capture_output=True, text=True, check=False
    )
    status = subprocess.run(
        ["git", "status", "--porcelain"], cwd=target,
        capture_output=True, text=True, check=False
    )
    license_files = [name for name in LICENSE_NAMES if (target / name).is_file()]
    return {
        "id": project["id"], "name": project["name"], "cloned": True,
        "path": str(target),
        "branch": branch.stdout.strip() if branch.returncode == 0 else None,
        "dirty": bool(status.stdout.strip()) if status.returncode == 0 else None,
        "license_files": license_files,
    }


def cmd_status(args: argparse.Namespace) -> int:
    destination = Path(args.destination)
    states = [local_project_state(p, destination) for p in PROJECTS]
    if args.json:
        print(json.dumps(states, indent=2))
        return 0
    print(f"Local source status — {destination.expanduser().resolve()}\n")
    for state in states:
        if not state["cloned"]:
            marker, details = "[--]", "not cloned"
        else:
            marker = "[OK]" if not state["dirty"] else "[DIRTY]"
            details = f"branch={state['branch'] or 'unknown'}"
            if state["dirty"]:
                details += ", local changes present"
        print(f"{marker:<9} {state['id']:<23} {details}")
    count = sum(1 for state in states if state["cloned"])
    print(f"\n{count}/{len(states)} projects cloned.")
    return 0


def cmd_audit(args: argparse.Namespace) -> int:
    destination = Path(args.destination)
    states = [local_project_state(p, destination) for p in PROJECTS]
    cloned = [state for state in states if state["cloned"]]
    if not cloned:
        print("No source repositories cloned yet. Use cheeku-infinity clone <id>.")
        return 0
    missing, dirty = [], []
    for state in cloned:
        if not state["license_files"]:
            missing.append(state["id"])
        if state["dirty"]:
            dirty.append(state["id"])
        label = ", ".join(state["license_files"]) if state["license_files"] else "NO COMMON LICENSE/NOTICE FILE FOUND"
        print(f"{state['id']}: {label}")
    if missing:
        print("\nReview upstream license terms manually for: " + ", ".join(missing))
    if dirty:
        print("Local modifications detected in: " + ", ".join(dirty))
    print("\nThis is a filename-presence check, not a legal determination or license parser.")
    return 0


def cmd_doctor(_: argparse.Namespace) -> int:
    checks = [
        ("Python >= 3.10", sys.version_info >= (3, 10), sys.version.split()[0]),
        ("Git", bool(shutil.which("git")), shutil.which("git") or "not found"),
        ("Catalogue", len(PROJECTS) == 16, f"{len(PROJECTS)} entries"),
    ]
    failures = 0
    print(f"CHEEKU INFINITY doctor — v{__version__}\n")
    for label, ok, detail in checks:
        print(f"{'[OK]' if ok else '[MISSING]':<10} {label}: {detail}")
        failures += not ok
    return 1 if failures else 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="cheeku-infinity",
        description="Discover and manage the curated CHEEKU INFINITY source collection."
    )
    parser.add_argument("--version", action="version", version=f"CHEEKU INFINITY {__version__}")
    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("list", help="List all catalogue projects")
    p.add_argument("--kind", choices=("skill", "tool", "application"))
    p.add_argument("--domain", help="Filter by domain name")
    p.add_argument("--json", action="store_true", help="Print machine-readable JSON")
    p.set_defaults(func=cmd_list)

    p = sub.add_parser("info", help="Show project details")
    p.add_argument("project")
    p.set_defaults(func=cmd_info)

    p = sub.add_parser("clone", help="Clone upstream source code")
    p.add_argument("project", nargs="?")
    p.add_argument("--all", action="store_true", help="Clone every catalogue project")
    p.add_argument("--destination", default=str(DEFAULT_DESTINATION))
    p.set_defaults(func=cmd_clone)

    p = sub.add_parser("update", help="Fast-forward cloned repositories")
    p.add_argument("project", nargs="?")
    p.add_argument("--all", action="store_true", help="Update all cloned projects")
    p.add_argument("--destination", default=str(DEFAULT_DESTINATION))
    p.set_defaults(func=cmd_update)

    p = sub.add_parser("status", help="Show cloned repositories and local changes")
    p.add_argument("--destination", default=str(DEFAULT_DESTINATION))
    p.add_argument("--json", action="store_true")
    p.set_defaults(func=cmd_status)

    p = sub.add_parser("audit", help="Check common license files and local Git changes")
    p.add_argument("--destination", default=str(DEFAULT_DESTINATION))
    p.set_defaults(func=cmd_audit)

    p = sub.add_parser("doctor", help="Check basic local prerequisites")
    p.set_defaults(func=cmd_doctor)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
