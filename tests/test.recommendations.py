import unittest
from aquarium_models import create_aquarium
from aquarium_recommendations import find_fish, get_plants, get_equipment, calculate_cost, budget_status

class RecommendationsTest(unittest.TestCase):
    def test_find_fish_filters_by_tank_size(self):
        aquarium = create_aquarium("freshwater", 5, 100)
        self.assertEqual([fish["name"] for fish in find_fish(aquarium)], ["Betta"])

    def test_equipment_depends_on_type(self):
        freshwater = get_equipment("freshwater")
        saltwater= get_equipment("saltwater")
        self.assertIn("dechlorinator", freshwater)
        self.assertIn("marine salt", saltwater)

    def test_unkown_plant_type_taises_error(self):
        with self.assertRaises(ValueError):
            get_plants("brackish")

    def test_budget_status_(self):
        aquarium = create_aquarium("freshwater", 20, 1000)
        self.assertEqual(budget_status(aquarium), "This estimate is within your budget.")
        self.assertEqual(calculate_cost(aquarium), 20)

if __name__ == "__main__":
    unittest.main()