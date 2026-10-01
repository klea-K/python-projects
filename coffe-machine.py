MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

units = {
    "water": "ml",
    "milk": "ml",
    "coffee": "g",
}

def check_ingredients(drink):
    """Check if the ingredients are enough for making the drink"""
    if MENU[drink]["ingredients"]["water"] >= resources["water"]:
        return f"Sorry there is not enough water"
    elif "milk" in MENU[drink] and MENU[drink]["ingredients"]["milk"] >= resources["milk"]:
        return f"Sorry there is not enough milk"
    elif MENU[drink]["ingredients"]["coffee"] >= resources["coffee"]:
        return f"Sorry there is not enough coffee"
    else:
        return True

def calculate_pay(drink):
    """Money calculation"""
    total_pay = int(input("How many quarters?:")) * 0.25
    total_pay += int(input("How many dimes?:")) * 0.10
    total_pay += int(input("How many nickles?:")) * 0.05
    total_pay += int(input("How many pennies?:")) * 0.01
    drink_cost = float(MENU[drink]["cost"])
    if total_pay < drink_cost:
        return f"Sorry that's not enough money. Money refunded."
    else:
        change = total_pay - drink_cost
        change = round(change,2)
        return change

def make_a_drink(drink):
    result = check_ingredients(drink)
    if result != True:
        print(result)
        return

    print("Please insert coins")
    change = calculate_pay(drink)
    drink_price = MENU[drink]["cost"]
    if isinstance(change,str):
        print(change)
        return

    print(f"Here is ${change} in change")
    print(f"Here is your {drink} ☕️. Enjoy!")

    global machine_money
    machine_money += drink_price

    for ingredients,amount in MENU[drink]["ingredients"].items():
        resources[ingredients] -= amount

machine_money = 0
machine_works = True
while machine_works:
    user_choice = input("What would you like? (espresso/latte/cappuccino):")
    if user_choice == 'off':
        machine_works = False
    elif user_choice == 'report':
        for key, value in resources.items():
            print(f"{key.capitalize()}: {value}{units[key]}")
        print(f"Money: ${machine_money}")
    else:
        make_a_drink(user_choice)