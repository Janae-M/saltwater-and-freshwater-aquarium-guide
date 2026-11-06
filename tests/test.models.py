import unittest
from aquarium_models import Aquarium, FreshwaterAquarium, SaltwaterAquarium, create_aquarium

class AquariumModelTests(unittest.TestCase):
    def test_factory_creates_freshwater_subclass(self):
        aquarium = create_aquarium("freshwater", 20, 200)
        self.assertIsInstance(aquarium, FreshwaterAquarium)
        self.assertEqual(aquarium.aquarium_type, "freshwater")

    def test_factory_creates_saltwater_subclass(self):
        aquarium = create_aquarium("saltwater", 30, 500)
        self.assertIsInstance(aquarium, SaltwaterAquarium)

    def test_invalid_type_raises_error(self):
        with self.assertRaises(ValueError):
            create_aquarium("brackish", 20, 200)

    def test_non_positive_size_raises_error(self):
        with self.assertRaises(ValueError):
            create_aquarium("freshwater", 0, 200)

    def test_cost_calculation(self):
        aquarium = create_aquarium("freshwater", 20, 500)
        aquarium.equipment = ["filter", "heater"]
        aquarium.fish = [{"name": "Betta"}]
        aquarium.decorations = [{"name": "Java Fern"}]
        self.assertEqual(aquarium.estimated_cost(), 40 + 50 + 15 + 10)

    def test_to_dict_and_from_dict(self):
        original = create_aquarium("saltwater", 30, 400)
        original.equipment = ["tank"]
        restored = Aquarium.from_dict(original.to_dict())
        self.assertIsInstance(restored, SaltwaterAquarium)
        self.assertEqual(restored.tank_size, 30)
        self.assertEqual(restored.equipment, ["tank"])

if __name__ == "__main__":
    unittest.main()