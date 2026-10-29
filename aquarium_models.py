"""
Freshwater or Saltwater Aquarium Guide
Janae Mireles
Data models for the Aquarium Guide.
October 28, 2026
"""
from dataclasses import dataclass, field
from typing import Any

@dataclass
class Aquarium:
    """contains the information shared by all aquarium plans."""
    tank_size: float
    budget: float
    fish: list[dict[str, Any]] = field(default_factory=list)
    decorations: list[dict[str, Any]] = field(default_factory=list)
    equipment: list[str] = field(default_factory=list)

    aquarium_type = "generic"

    def estimated_cost(self) -> float:
        """returns the projects estimated setup cost."""
        return (
            self.tank_size * 2
            + len(self.equipment) * 25
            + len(self.fish) * 15
            +len(self.decorations) * 10
        )

    def to_dict(self) -> dict[str, Any]:
        """converts the objects to JSON compatible data."""
        return {
            "type": self.aquarium_type,
            "tank_size": self.tank_size,
            "budget": self.budget,
            "fish": self.fish,
            "decorations": self.decorations,
            "equipment": self.equipment,
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "Aquarium":
        """creates the necessary subclasses from the saved data."""
        aquarium_type = data.get("type", "").lower()
        aquarium_class = {
            "freshwater": FreshwaterAquarium,
            "saltwater": SaltwaterAquarium,
        }.get(aquarium_type)
        if aquarium_class is None:
            raise ValueError("Aquarium type must be 'freshwater' or 'saltwater'.")

        return aquarium_class(
            tank_size = float(data["tank_size"]),
            budget = float(data["budget"]),
            fish = list(data.get("fish", [])),
            decorations = list(data.get("decorations", [])),
            equipment = list(data.get("equipment", [])),
        )
