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


def check_resources(drink, current_resources):
    if drink != "espresso":
        if ((current_resources['water'] - MENU[drink]['ingredients']['water']) < 0) or \
                ((current_resources['milk'] - MENU[drink]['ingredients']['milk']) < 0) or \
                ((current_resources['coffee'] - MENU[drink]['ingredients']['coffee']) < 0):
            return False
        else:
            return True
    else:
        if ((current_resources['water'] - MENU[drink]['ingredients']['water']) < 0) or \
                ((current_resources['coffee'] - MENU[drink]['ingredients']['coffee']) < 0):
            return False
        else:
            return True


def check_cost(drink, dollars, quarters, dimes, nickels):
    money_paid = (dollars * 1) + (quarters * 0.25) + (dimes * 0.1) + (nickels * 0.05)
    if money_paid < MENU[drink]['cost']:
        return False, money_paid
    else:
        return True, money_paid


def coffee_machine(resources):
    resources["cost"] = 0
    while True:
        choice = input("What would you like? (espresso/latte/cappuccino): ")
        if choice == "off":
            return
        elif choice == "report":
            print(f"Current Report\nWater: {resources['water']} ml\nMilk: {resources['milk']} ml\nCoffee: "
                  f"{resources['coffee']} g\nCost: ${'%.2f' % resources['cost']}")
        else:
            if not check_resources(choice, resources):
                print("Sorry, Not enough resources, input report to check available resources")
            else:
                print(f"{choice} costs ${MENU[choice]['cost']}\nNote this machine only takes coins\n")
                dollars = int(input("How many Dollars? "))
                quarters = int(input("How many Quarters? "))
                dimes = int(input("How many Dimes? "))
                nickels = int(input("How many Nickels? "))
                cost = check_cost(choice, dollars, quarters, dimes, nickels)
                if not cost[0]:
                    print(f"Sorry {choice} costs ${MENU[choice]['cost']}, You gave S{'%.2f' % cost[1]}, Money Refunded")
                else:
                    resources["water"] -= MENU[choice]["ingredients"]["water"]
                    if len(MENU[choice]['ingredients']) > 2:
                        resources["milk"] -= MENU[choice]["ingredients"]["milk"]
                    resources["coffee"] -= MENU[choice]["ingredients"]["coffee"]
                    resources["cost"] += cost[1]
                    print(f"\nHere is your {choice}, your refund is ${'%.2f' % (cost[1] - MENU[choice]['cost'])}")


coffee_machine(resources)
