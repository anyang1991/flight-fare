"""Exercise installation failures that would prevent another user loading the skill."""

import shutil
import tempfile
import unittest
from pathlib import Path

from scripts.validate import validate


REPO = Path(__file__).resolve().parents[1]
NAME = "flight-fullfare-screenshot"
HEADER = f"---\nname: {NAME}\ndescription: 查询官网全价截图\n---\n"


class ValidationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / NAME
        self.root.mkdir()
        self.write("SKILL.md", HEADER + "说明\n")

    def write(self, name, text):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")

    def test_minimal_installed_skill(self):
        self.assertEqual(validate(self.root, installed=True), [])

    def test_installed_copy_with_all_supporting_files(self):
        for name in ("SKILL.md", "README.md", "LICENSE"):
            shutil.copy2(REPO / name, self.root / name)
        for name in ("agents", "references", "examples", "tests"):
            shutil.copytree(REPO / name, self.root / name, ignore=shutil.ignore_patterns("__pycache__"))
        self.assertEqual(validate(self.root, installed=True), [])

    def test_directory_name_mismatch(self):
        wrong = self.root.rename(self.root.with_name("flight-fare"))
        self.assertTrue(validate(wrong, installed=True))
        self.assertEqual(validate(wrong), [])  # repo checkouts may have another name

    def test_missing_frontmatter(self):
        self.write("SKILL.md", "# 无元数据\n")
        self.assertTrue(validate(self.root))

    def test_duplicate_metadata_key(self):
        self.write("SKILL.md", HEADER.replace("description:", "name: other\ndescription:") + "说明")
        self.assertTrue(validate(self.root))

    def test_non_string_description(self):
        self.write("SKILL.md", HEADER.replace("查询官网全价截图", "[one, two]") + "说明")
        self.assertTrue(validate(self.root))

    def test_blank_description(self):
        self.write("SKILL.md", HEADER.replace("查询官网全价截图", "''") + "说明")
        self.assertTrue(validate(self.root))

    def test_missing_reference(self):
        self.write("SKILL.md", HEADER + "[入口](references/missing.md)")
        self.assertTrue(validate(self.root))

    def test_encoded_unicode_reference(self):
        self.write("references/中文.md", "入口")
        self.write("SKILL.md", HEADER + "[入口](references/%E4%B8%AD%E6%96%87.md#section)")
        self.assertEqual(validate(self.root), [])

    def test_reference_cannot_escape_package(self):
        (self.root.parent / "outside.md").write_text("exists", encoding="utf-8")
        self.write("SKILL.md", HEADER + "[外部](../outside.md)")
        self.assertTrue(validate(self.root))

    def test_declared_license_must_ship(self):
        self.write("SKILL.md", HEADER.replace("---\nname:", "---\nlicense: MIT\nname:") + "说明")
        self.assertTrue(validate(self.root))

    def test_ui_prompt_must_route_to_installed_skill(self):
        self.write("agents/openai.yaml", "interface:\n  display_name: 示例\n  short_description: 说明\n  default_prompt: 使用 $wrong-name\n")
        self.assertTrue(validate(self.root))

    def test_utf8_bom_rejected(self):
        self.write("SKILL.md", "\ufeff" + HEADER + "说明")
        self.assertTrue(validate(self.root))

    def test_repository(self):
        self.assertEqual(validate(REPO), [])


if __name__ == "__main__":
    unittest.main()
