import hashlib
import json
import shutil
import tempfile
import unittest
from pathlib import Path

from scripts.validate import validate

ROOT = Path(__file__).resolve().parents[1]


class RepositoryChecks(unittest.TestCase):
    def test_repository_passes(self):
        self.assertEqual(validate(ROOT), [])

    def test_original_eleven_skills_unchanged(self):
        snapshot = json.loads((ROOT / "tests/fixtures/legacy-skills.json").read_text())
        self.assertEqual(len(snapshot), 11)
        for relative, digest in snapshot.items():
            with self.subTest(skill=relative):
                self.assertEqual(hashlib.sha256((ROOT / relative).read_bytes()).hexdigest(), digest)

    def test_pre_150_skills_unchanged(self):
        snapshot = json.loads((ROOT / "tests/fixtures/pre-1.5.0-skills.json").read_text())
        self.assertEqual(len(snapshot), 13)
        for relative, digest in snapshot.items():
            with self.subTest(skill=relative):
                self.assertEqual(hashlib.sha256((ROOT / relative).read_bytes()).hexdigest(), digest)

    def check_mutation(self, mutate, expected):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for relative in ("skills", ".claude-plugin", ".codex-plugin", ".agents/plugins"):
                shutil.copytree(ROOT / relative, root / relative)
            for path in ROOT.glob("*.md"):
                if path.name not in {"implementation-notes.md", "FUTURE-EXTENSIONS.md"}:
                    shutil.copy2(path, root / path.name)
            shutil.copy2(ROOT / "LICENSE", root / "LICENSE")
            mutate(root)
            self.assertTrue(any(expected in error for error in validate(root)), expected)

    def test_missing_ship_gate_entry_is_rejected(self):
        def mutate(root):
            path = root / ".claude-plugin/plugin.json"
            data = json.loads(path.read_text())
            data["skills"].pop()
            path.write_text(json.dumps(data))
        self.check_mutation(mutate, "ship gate")

    def test_duplicate_ship_gate_entry_is_rejected(self):
        def mutate(root):
            path = root / ".claude-plugin/plugin.json"
            data = json.loads(path.read_text())
            data["skills"].append(data["skills"][0])
            path.write_text(json.dumps(data))
        self.check_mutation(mutate, "ship gate")

    def test_version_drift_is_rejected(self):
        def mutate(root):
            path = root / ".codex-plugin/plugin.json"
            data = json.loads(path.read_text())
            data["version"] = "9.9.9"
            path.write_text(json.dumps(data))
        self.check_mutation(mutate, "agree on version")

    def test_duplicate_yaml_key_is_rejected(self):
        def mutate(root):
            path = root / "skills/assumption-test/SKILL.md"
            path.write_text(path.read_text().replace("name: assumption-test", "name: assumption-test\nname: other"))
        self.check_mutation(mutate, "duplicate or non-string YAML key")

    def test_directory_name_mismatch_is_rejected(self):
        def mutate(root):
            path = root / "skills/assumption-test/SKILL.md"
            path.write_text(path.read_text().replace("name: assumption-test", "name: other"))
        self.check_mutation(mutate, "name must match directory")

    def test_broken_link_is_rejected(self):
        def mutate(root):
            path = root / "README.md"
            path.write_text(path.read_text() + "\n[missing](does-not-exist.md)\n")
        self.check_mutation(mutate, "broken local link does-not-exist.md")

    def test_maintainer_instruction_drift_is_rejected(self):
        def mutate(root):
            path = root / "AGENTS.md"
            path.write_text(path.read_text() + "\nDrift\n")
        self.check_mutation(mutate, "byte-identical")

    def test_stale_readme_count_is_rejected(self):
        def mutate(root):
            path = root / "README.md"
            path.write_text(path.read_text().replace(f"**{len(list((root / 'skills').glob('*/SKILL.md')))} installable", "**0 installable"))
        self.check_mutation(mutate, "headline skill count")


if __name__ == "__main__":
    unittest.main()
