import json
import unittest
from pathlib import Path

from cheeku_infinity.catalog import PROJECTS, PROJECT_BY_ID


class CatalogTests(unittest.TestCase):
    def test_catalog_has_sixteen_unique_projects(self):
        self.assertEqual(len(PROJECTS), 16)
        self.assertEqual(len(PROJECT_BY_ID), 16)

    def test_project_metadata_is_complete(self):
        required = {"id", "name", "repository", "url", "branch", "kind", "domain", "description", "setup"}
        for project in PROJECTS:
            with self.subTest(project=project["id"]):
                self.assertTrue(required.issubset(project))
                self.assertIn(project["kind"], {"skill", "tool", "application"})
                self.assertTrue(project["url"].startswith("https://github.com/"))

    def test_documented_kind_totals(self):
        counts = {kind: sum(p["kind"] == kind for p in PROJECTS)
                  for kind in ("skill", "tool", "application")}
        self.assertEqual(counts, {"skill": 7, "tool": 6, "application": 3})

    def test_known_default_branches(self):
        self.assertEqual(PROJECT_BY_ID["minimind"]["branch"], "master")
        self.assertEqual(PROJECT_BY_ID["nginx"]["branch"], "master")
        self.assertEqual(PROJECT_BY_ID["openvino"]["branch"], "master")
        self.assertEqual(PROJECT_BY_ID["affine"]["branch"], "canary")

    def test_json_manifest_has_same_ids(self):
        path = Path(__file__).resolve().parents[1] / "catalog.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        self.assertEqual([p["id"] for p in data["projects"]],
                         [p["id"] for p in PROJECTS])


if __name__ == "__main__":
    unittest.main()
