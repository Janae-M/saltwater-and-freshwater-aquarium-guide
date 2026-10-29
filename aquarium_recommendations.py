"""
Freshwater or Saltwater Aquarium Guide
Janae Mireles
Functions for recommendations and calculations 
October 28, 2026
"""
from aquarium_data import FISH_DATABASE, PLANTS, AQUARIUM_EQUIPMENT
from aquarium_models import Aquarium 

def find_fish(aquarium: Aquarium) -> list[dict]:
    """returns fish entries whos listed minimum tank size is acceptable for the plan."""
    return [
        fish for fish in FISH_DATABASE[aquarium.aquarium_type]
        if aquarium.tank_size >= fish["minimum_gallons"]
    ]

def get_plants(aquarium_type: str) -> list[dict]:
    """returns the plant options that are supported by the aquarium type"""
    try:
        return [plant.copy() for plant in PLANTS[aquarium_type.lower()]]
    except KeyError as exc:
        raise ValueError("Aquarium type must be 'freshwater' or 'saltwater'.") from exc

def get_equipment(aquarium_type: str) -> list[str]:
    """returns a list of standard equipment for the aquarium type."""
    try:
        return list(AQUARIUM_EQUIPMENT[aquarium_type.lower()])
    except KeyError as exc:
        raise ValueError("Aquarium type must be 'freshwater' or 'saltwater'.") from exc

def calculate_cost(aquarium: Aquarium) -> float:
    """returns the estimated cost for the users plan."""
    return aquarium.estimated_cost()

def budget_status(aquarium: Aquarium) -> str:
    """describes whether the estimate is or is not within the users budget."""
    if calculate_cost(aquarium) <= aquarium.budget:
        return "This estimate is within your budget."
    return "This estimate is over your budget."