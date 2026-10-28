"""
Freshwater or Saltwater Aquarium Guide
Janae Mireles
References the data for building an aquarium.
October 28, 2026
"""

FISH_DATABASE = {
    "freshwater": [
        {"name": "Tetras", "minimum_gallons": 20, "fahrenheit": 72},
        {"name": "Betta", "minimum_gallons": 5, "fahrenheit": 80},
        {"name": "Danios", "minimum_gallons": 20, "fahrenheit": 70},
        {"name": "Platys", "minimum_gallons": 20, "fahrenheit": 80},
        {"name": "Corydoras", "minimum_gallons": 20, "fahrenheit": 75},
    ],
    "saltwater": [
        {"name": "Clownfish", "minimum_gallons": 20, "Salinity": 1.025},
        {"name": "Gramma", "minimum_gallons": 30, "Salinity": 1.025},
        {"name": "Firefish", "minimum_gallons": 20, "Salinity": 1.020},
        {"name": "Banggai", "minimum_gallons": 30, "Salinity": 1.023},
        {"name": "Elacatinus", "minimum_gallons": 10, "Salinity": 1.023},
    ],
}

PLANTS = {
    "freshwater": [
        {"name": "Java Fern", "lighting": "low"},
        {"name": "Anubias", "lighting": "low"},
        {"name": "Amazon Swords", "lighting": "moderate"},
    ],
    "saltwater": [
        {"name": "Eelgrass", "lighting": "high"},
        {"name": "Chaetomorpha", "lighting": "moderate"},
        {"name": "Mangroves", "lighting": "moderate"},
    ],
}

AQUARIUM_EQUIPMENT = {
    "freshwater": (
        "tank", "filtration", "heater", "LED lighting", "substrate",
        "test kits", "dechlorinator",
    ),
    "saltwater": (
        "tank", "filtration", "heater", "LED lighting", "substrate",
        "test kits", "live rock", "protein skimmer", "circulation pump",
        "marine salt",
    ),
}
