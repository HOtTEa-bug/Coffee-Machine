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

profit = 0 #global


def check_resources(ordered_ingredients):
    for item in ordered_ingredients:
        if resources["water"]< ordered_ingredients["water"] :
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    print("\nPlease insert coins.")
    total = int(input("How many quarters($0.25)?: ")) * 0.25
    total += int(input("How many dimes($0.10)?: ")) * 0.1
    total += int(input("How many nickles($0.05)?: ")) * 0.05
    total += int(input("How many pennies($0.01)?: ")) * 0.01
    return total


def transaction_successful(payment_received , drink_cost):
    if payment_received < drink_cost:
        print(" Sorry that's not enough money. Money refunded.")
        return False
    else:
        change = round(payment_received - drink_cost, 2)
        if change>0: 
            print(f"-----Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    
def make_coffee(drink_ordered, drink_ingredients):
    # Keep track of resources used
    for item in drink_ingredients:
        resources[item] -= drink_ingredients[item]
    print(f"\nHere is your {drink_ordered} ☕️. Enjoy!")


# Driver
machine_on = True

while machine_on:
    print("\n \n-----Hello Customer------\n\n")
    # Prompt user by asking

    choice = input("Display: \n 1. Espresso- $1.50 \n 2. Latte- $2.50\n 3. Cappuccino- $3.00 \nWhat would you like?: ").lower()

    # Turn off the Coffee Machine by entering “off” to the prompt.
    if choice == "off":
        machine_on = False
    elif choice == "report":
        print(f"\nWater: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]

        # Check for sufficient resources. If sufficient resource process coins
        if check_resources( drink["ingredients"]) :
            payment = process_coins()
            # Check transaction successful?
            if transaction_successful(payment, drink["cost"]):
                # Make Coffee
                make_coffee(choice, drink["ingredients"])
        
        
