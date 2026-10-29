"""
Freshwater or Saltwater Aquarium Guide
Janae Mireles
Guides users through the process of setting up and maintaining a freshwater or saltwater aquarium, including selecting the right fish, plants, and equipment for their specific needs.
September 25th,2026
"""
from aquarium_data import PLANTS
from aquarium_models import Aquarium

aquarium = {
    "type": "",
    "tank size": 0,
    "budget": 0,
    "decorations": [],
    "fish": [],
    "equipment": []
}

def welcome_message():

    print("\n" + "-" * 40)
    print("WELCOME TO AQUARIUM GUIDE")
    print("-" * 40)

    print("\nThis program will guide you through the process of setting up and maintaining a freshwater or " \
    "saltwater aquarium, including selecting the right fish, plants, and equipment for your specific needs!")

def user_aquarium_type():
    """asks users to choose between a freshwater or saltwater aquarium"""
    while True:
        aquarium_type = input(
            "\nWould you like to create a freshwater or saltwater aquarium? "
        ).lower()
        if aquarium_type == "freshwater":
            return aquarium_type
        elif aquarium_type == "saltwater":
            return aquarium_type
        else:
            print("Please enter either 'freshwater' or 'saltwater'.")

def user_tank_size():
    """retrieves users prefered tank size by gallons"""
    while True:
        try:
            size = float(input(
                "\nHow many gallons of water will your tank contain? "
            ))
            if size > 0:
                return size
            else:
                print("Tank size must be greater than 0.")

        except ValueError:
            print("Please enter a number.")

def user_budget():
    """users budget for their aquarium build"""
    while True:
        try:
            budget = float(input(
                "\nWhat is your budget (in dollars) for this build? "
            ))
            if budget > 0:
                return budget 
            else:
                print("Budget must be greater than 0.")
        except ValueError:
            print("Please enter a number. ")

def user_decorations(aquarium_type):
    """users choices for freshwater or saltwater plants, allows multiple options"""
    options = plants[aquarium_type]
    selected = []

    if aquarium_type == "freshwater":
        category = "plants"
    else:
        category = "saltwater plants"
    while True:
        print("\nChoose your", category + ":")

        for number in range(len(options)):
            print(
                number + 1,
                ".",
                options[number]["name"],
                "- Lighting:",
                options[number]["lighting"]
            )

        print("0. Done")

        choice = input("Enter your choice: ")

        if choice.isdigit():

            choice = int(choice)

            if choice == 0:
                break
            elif 1 <= choice <= len(options):
                selected.append(options[choice - 1])
                print(
                    options[choice -1]["name"], "added!"
                )
            else:
                print("Invalid choice.")

        else:
            print("Please enter a number.")

    return selected

def find_fish(aquarium):
    """valid fish based on aquarium type and size""" 
    aquarium_type = aquarium["type"]
    tank_size = aquarium["tank size"]

    possible_fish = []

    for fish in fish_database[aquarium_type]:
        if tank_size >= fish["minimum_gallons"]:
            possible_fish.append(fish)

    return possible_fish

def user_fish_choice(aquarium):
    """Allows users to select compatible fish for their aquarium based on the users aquarium information"""
    fish_options = find_fish(aquarium)
    selected_fish = []

    if len(fish_options) == 0:
        print("\nThere are no fish available for this tank size")
        return selected_fish
    
    while True:
        print("\nFish available for your aquarium:")

        for number in range(len(fish_options)):
            fish = fish_options[number]
            print(
                number + 1,
                ".",
                fish["name"],
                "- Minimum:",
                fish["minimum_gallons"],
                "gallons"
            )

        print("0. Done")

        choice = input("choose a fish:")

        if choice.isdigit():
            choice = int(choice)

            if choice == 0:
                break

            elif 1 <= choice <= len(fish_options):
                fish = fish_options[choice - 1]
                
                if fish not in selected_fish:
                    selected_fish.append(fish)
                    print(fish["name"], "added!")

                else:
                    print("You have already selected that fish.")

            else:
                print("Invalid chooice.")

        else:
            print("Please enter a number.")
    return selected_fish

def user_equipment(aquarium_type):

    equipment = []

    for item in aquarium_equipment[aquarium_type]:
        equipment.append(item)

    return equipment

def calculate_cost(aquarium):
    """calculates the total estimated cost of the users entire aquarium build"""
    tank_size = aquarium["tank size"]

    tank_cost = tank_size * 2
    equipment_cost = len(aquarium["equipment"]) * 25
    fish_cost = len(aquarium["fish"]) * 15
    decoration_cost = len(aquarium["decorations"]) * 10 

    total = (tank_cost + equipment_cost + fish_cost + decoration_cost)

    return total

def display_fish(aquarium):

    print("\n" + "-" * 40)
    print("RECOMMENDED FISH:")
    print("-" * 40)

    if len(aquarium["fish"]) == 0:
        print("No fish were selected.")

    else:
        for fish in aquarium["fish"]:
            print("\nName:", fish["name"])
            print(
                "Minimum tank size",
                fish["minimum_gallons"],
                "gallons"
            )

            if aquarium["type"] == "freshwater":
                print(
                    "Temperature:",
                    fish["fahrenheit"],
                    "F"
                )
            else:
                print(
                    "Salinity:",
                    fish["Salinity"]
                )

def display_decorations(aquarium):

    print("\n" + "-" * 40)

    if aquarium["type"] == "freshwater":
        print("SELECTED PLANTS")
    else:
        print("SELECTED SALTWATER PLANTS")

    print("-" * 40)

    if len(aquarium["decorations"]) == 0:
        print("No plants were selected.")
    else:
        for decoration in aquarium["decorations"]:
            print("\nName:", decoration["name"])
            print(
                "Lighting:",
                decoration["lighting"]
            )

def display_equipment(aquarium):

    print("\n" + "-" * 40)
    print("RECOMMENDED EQUIPMENT")
    print("-" * 40)

    for item in aquarium["equipment"]:
        print("-", item)

def display_plan(aquarium):

    print("\n" + "-" * 40)
    print("YOUR AQUARIUM PLAN")
    print("-" * 40)

    print("\nAquarium type:", aquarium["type"])
    print("Tank size:", aquarium["tank size"], "gallons")
    print("Budget: $", format(aquarium["budget"], ".2f"))

    display_fish(aquarium)
    display_decorations(aquarium)
    display_equipment(aquarium)
    cost = calculate_cost(aquarium)

    print("\n" + "-" * 40)
    print("ESTIMATED COST")
    print("-" * 40)

    print("$", format(cost, ".2f"))

    if cost <= aquarium["budget"]:
        print("This estimate is within your budget.")
    else:
        print("This estimate is over your budget.")

def advice(aquarium):
    """Outputs general advice based on users selections."""
    print("\n" + "-" * 40)
    print("AQUARIUM ADVICE")
    print("-" * 40)

    if aquarium["type"] == "freshwater":
        print("Remember to treat tap water with a proper dechlorinator before adding fish.")

    else:
        print("You must monitor the salinity carefully in a saltwater aquarium. The water will evaporat, but " \
        "salt stays behind. It's best to replace evaporated water with RO/DI water.")

    if aquarium["tank size"] < 20:
        print("Smaller tanks require more attention, as the water conditions may quickly change.")

    else:
        print("Larger tanks generally provide more room for varity and are easier to maintain.")

    if len(aquarium["decorations"]) > 0:
        print("Check that your lighting matches the needs of your selected plants and organisms.")

def create_aquarium():

    aquarium["type"] = user_aquarium_type()

    aquarium["tank size"] = user_tank_size()

    aquarium["budget"] = user_budget()

    aquarium["decorations"] = user_decorations(aquarium["type"])

    aquarium["fish"] = user_fish_choice(aquarium)

    aquarium["equipment"] = user_equipment(aquarium["type"])

    return aquarium

def main():

    welcome_message()

    create_aquarium()

    display_plan(aquarium)

    advice(aquarium)

    print("\nThank you for using Aquarium Guide, goodbye!")

main()