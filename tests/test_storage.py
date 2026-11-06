import json
import tempfile
import unittest
from pathlib import Path
from aquarium_models import create_aquarium, FreshwaterAquarium
from user_storage import save_plan, load_plan, save_summary

class StorageTests(unittest.TestCase):
    def test_json_round_trip(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "aquarium_plan.json"
            original = create_aquarium("freshwater", 20, 250)
            original.fish = [{"name": "Tetras", "minimum_gallons": 20}]
            save_plan(original, path)
            restored = load_plan(path)
            self.assertIsInstance(restored, FreshwaterAquarium)
            self.assertEqual(restored.fish[0]["name"], "Tetras")

    def test_missing_file_raises_friendly_error(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "missing.json"
            with self.assertRaises(FileNotFoundError):
                load_plan(path)

    def test_invalid_json_raises_value_error(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "negative.json"
            path.write_text("not a json", encoding="utf-8")
            with self.assertRaises(ValueError):
                load_plan(path)

    def test_text_summary_is_written(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "aquarium_summary.txt"
            aquarium = create_aquarium("saltwater", 30, 400)
            save_summary(aquarium, path)
            self.assertIn("Aquarium type: saltwater", path.read_text(encoding="utf-8"))

if __name__ == "__main__":
    unittest.main()