import Data

power = 1
WATER = Data.resources["water"]
MILK = Data.resources["milk"]
COFFEE = Data.resources["coffee"]
MONEY = 0


def coffee_machine():
    resources_ok = 0
    global MONEY
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if user_choice == "espresso":
        data = copy_data(user_choice)
        resources_ok = check_resources(data[0], data[1], data[2])
    elif user_choice == "latte":
        data = copy_data(user_choice)
        resources_ok = check_resources(data[0], data[1], data[2])
    elif user_choice == "cappuccino":
        data = copy_data(user_choice)
        resources_ok = check_resources(data[0], data[1], data[2])
    elif user_choice == "off":
        return 0
    elif user_choice == "report":
        print(f"Milk: {MILK}ml")
        print(f"Water: {WATER}ml")
        print(f"Coffee: {COFFEE}ml")
        print(f"Money: ${MONEY}")
        return 1

    if resources_ok:
        print("Please insert coins.")
        quarters = int(input("How many quarters?: ")) * 0.25
        dimes = int(input("How many dimes?: ")) * 0.1
        nickles = int(input("How many nickles?: ")) * 0.05
        pennies = int(input("How many pennies?: ")) * 0.01
        MONEY = quarters + dimes + nickles + pennies
    else:
        return 0


def check_resources(water, milk, coffee):
    if water > Data.resources["water"]:
        print("not enough water.")
        return 0
    elif milk > Data.resources["milk"]:
        print("not enough water.")
        return 0
    elif coffee > Data.resources["coffee"]:
        print("not enough coffee.")
        return 0
    else:
        return 1


def copy_data(choice):
    water_needed = Data.resources[choice]["ingredients"]["water"]
    milk_needed = Data.resources[choice]["ingredients"]["milk"]
    coffee_needed = Data.resources[choice]["ingredients"]["coffee"]
    money_needed = Data.resources[choice]["cost"]
    return water_needed, milk_needed, coffee_needed, money_needed


print("☕Coffee machine program V1.0☕")
while power:
    power = coffee_machine()
