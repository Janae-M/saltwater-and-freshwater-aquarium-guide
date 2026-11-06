"""
Freshwater or Saltwater Aquarium Guide
Janae Mireles
Guides users through the process of setting up and maintaining a freshwater or saltwater aquarium, including selecting the right fish, plants, and equipment for their specific needs.
September 25th, 2026
"""
from aquarium_data import PLANTS
from aquarium_models import Aquarium, create_aquarium
from aquarium_recommendations import find_fish, get_equipment, budget_status
from user_storage import save_plan, save_summary

def ask_aquarium_type() -> str:
    """asks the user to select an aquarium type."""
    while True:
        choice = input("\nWould you like to create a freshwater or saltwater aquirium? ").strip().lower()
        if choice in ("freshwater", "saltwater"):
            return choice
        print("Invalid input. Please enter 'freshwater' or 'saltwater'.")

def ask_positive_number(prompt: str) -> float:
    """asks the user to enter a positive number."""
    while True:
        try:
            number = float(input(prompt))
            if number > 0:
                return number
            print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def choose_items(options: list[dict], label: str) -> list[dict]:
    """allows the user to select items from a list of options."""
    selected = []
    while True:
        print(f"\nChoose {label}:")
        for index, item in enumerate(options, start=1):
            extra = item.get("lighting")
            if extra:
                print(f"{index}. {item['name']} - Lighting: {extra}")
            else:
                print(f"{index}. {item['name']} - Minimum {item['minimum_gallons']} gallons")
        print("0. Done")

        choice = input("Enter your choice: ").strip()
        if not choice.isdigit():
            print("Invalid input. Please enter a number.")
            continue

        number = int(choice)
        if number == 0:
            return selected
        if not 1 <= number <= len(options):
            print("invalid choice.")
            continue

        item = options[number - 1]
        if item in selected:
            print("You have already selected that item.")
        else:
            selected.append(item.copy())
            print(f"{item['name']} added to your selection.")

def display_plan(aquarium: Aquarium) -> None:
    """displays the users aquarium plan."""
    print("\n" + "-" * 40)
    print("YOUR AQUARIUM PLAN")
    print("-" * 40)
    print(f"Aquarium type: {aquarium.aquarium_type}")
    print(f"Tank size: {aquarium.tank_size:g} gallons")
    print(f"Budget: ${aquarium.budget:.2f}")

    print("\nRECOMMENDED FISH")
    if aquarium.fish:
        for fish in aquarium.fish:
            print(f"- {fish['name']} (Minimum {fish['minimum_gallons']} gallons)")
            if "fahrenheit" in fish:
                print(f"  Temperature: {fish['fahrenheit']}°F")
            if "Salinity" in fish:
                print(f"  Salinity: {fish['Salinity']}")
    else:
        print("No fish selected.")

    print("\nSELECTED PLANTS")
    for plant in aquarium.decorations:
        print(f"- {plant['name']} (Lighting: {plant['lighting']})")
    if not aquarium.decorations:
        print("No plants selected.")

    print("\nRECOMMENDED EQUIPMENT")
    for item in aquarium.equipment:
        print(f"- {item}")

    print(f"\nEstimated cost: ${aquarium.estimated_cost():.2f}")
    print(budget_status(aquarium))
    print("\nCARE ADVICE")
    care_advice = getattr(aquarium, "care_advice", None)
    if callable(care_advice):
        print(care_advice())
    else:
        print("No specific care advice available.")

def run() -> None:
    """main function to run the aquarium guide."""
    print("-" * 40)
    print("WELCOME TO AQUARIUM GUIDE!")
    print("-" * 40)

    print("\nThis program will guide you through the process of setting up and maintaining a freshwater or " \
    "saltwater aquarium, including selecting the right fish, plants, and equipment for your specific needs!")

    aquarium_type = ask_aquarium_type()
    tank_size = ask_positive_number("\nHow many gallons will tank contain? ")
    budget = ask_positive_number("\nWhat is your budget for the aquarium in dollars? ")

    aquarium = create_aquarium(aquarium_type, tank_size, budget)
    plant_options = PLANTS[aquarium_type]
    aquarium.decorations = choose_items(plant_options, "plants")

    fish_options = find_fish(aquarium)
    aquarium.fish = choose_items(fish_options, "fish") if fish_options else []
    if not fish_options:
        print("\nNo fish options are available for the tank size you selected.")

    aquarium.equipment = get_equipment(aquarium_type)
    display_plan(aquarium)

    try:
        save_plan(aquarium)
        save_summary(aquarium)
        print("\nYour aquarium plan has been saved to 'aquarium_plan.json' and 'aquarium_summary.txt'.")
    except OSError as exc:
        print(f"\nYour plan was displayed, but could not be saved: {exc}")

    print("\nThank you for using the Aquarium Guide! Enjoy your new aquarium!")

if __name__ == "__main__":
    run()