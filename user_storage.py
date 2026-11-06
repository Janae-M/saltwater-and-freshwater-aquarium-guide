"""
Freshwater or Saltwater Aquarium Guide
Janae Mireles
Read and write aquarium plans as JSON files and human-readable text files.
November 5, 2026
"""
import json
from pathlib import Path
from aquarium_models import Aquarium

def save_plan(aquarium: Aquarium, filename: str | Path = "aquarium_plan.json") -> None:
    """saves the aquarium plan to a JSON file."""
    path = Path(filename)
    try:
        with path.open("w", encoding="utf-8") as file:
            json.dump(aquarium.to_dict(), file, indent=4)
    except OSError as exc:
        raise OSError(f"Failed to save the aquarium plan to '{path}': {exc}") from exc

def load_plan(filename: str |Path = "aquarium_plan.json") -> Aquarium:
    """loads the aquarium plan from a JSON file."""
    path = Path(filename)
    try:
        with path.open("r", encoding="utf-8") as file:
            data = json.load(file)
    except FileNotFoundError as exc:
        raise FileNotFoundError(f"The file '{path}' does not exist.") from exc
    except json.JSONDecodeError as exc:
        raise ValueError(f"Failed to decode JSON from '{path}': {exc}") from exc
    except OSError as exc:
        raise OSError(f"Failed to read the aquarium plan from '{path}': {exc}") from exc

    if not isinstance(data, dict):
        raise ValueError("Saved aquarium plan must be a JSON object.")
    try:
        return Aquarium.from_dict(data)
    except (KeyError, TypeError, ValueError) as exc:
        raise ValueError(f"Saved aquarium plan is missing required fields or has invalid data: {exc}") from exc

def save_summary(aquarium: Aquarium, filename: str | Path = "aquarium_summary.txt") -> None:
    """saves a human-readable summary of the aquarium plan to a text file."""
    path = Path(filename)
    lines = [
        "YOUR AQUARIUM PLAN",
        f"Aquarium type: {aquarium.aquarium_type}",
        f"Tank size: {aquarium.tank_size:g} gallons",
        f"Budget: ${aquarium.budget:.2f}",
        f"Fish: {', '.join(fish['name'] for fish in aquarium.fish) or 'None selected'}",
        f"Plants: {', '.join(plant['name'] for plant in aquarium.decorations) or 'None selected'}",
        f"Equipment: {', '.join(aquarium.equipment) or 'None listed'}",
        f"Estimated cost: ${aquarium.estimated_cost():.2f}",
    ]
    try:
        with path.open("w", encoding="utf-8") as file:
            file.write("\n".join(lines) + "\n")
    except OSError as exc:
        raise OSError(f"Failed to save the aquarium summary to '{path}': {exc}") from exc