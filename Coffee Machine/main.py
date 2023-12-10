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


def check_resources(coffee):
    if coffee == "espresso":
        if MENU["espresso"]["ingredients"]["water"] > resources["water"] or MENU["espresso"]["ingredients"]["coffee"] > \
                resources["coffee"]:
            print("Sorry, not enough resources are available!")
            return False
        else:
            print("Let's get this rolling!!")
            return True
    elif coffee == "latte":
        if MENU["latte"]["ingredients"]["water"] > resources["water"] or MENU["latte"]["ingredients"]["milk"] > \
                resources["milk"] or MENU["latte"]["ingredients"]["coffee"] > resources["coffee"]:
            print("Sorry, not enough resources are available!")
            return False
        else:
            print("Let's get this rolling!!")
            return True
    else:
        if MENU["cappuccino"]["ingredients"]["water"] > resources["water"] or MENU["cappuccino"]["ingredients"]["milk"] > \
                resources["milk"] or MENU["cappuccino"]["ingredients"]["coffee"] > resources["coffee"]:
            print("Sorry, not enough resources are available!")
            return False
        else:
            print("Let's get this rolling!!")
            return True


def check_money(coffee, cash, m):
    if coffee == "latte":
        cost = MENU["latte"]["cost"]
    elif coffee == "cappuccino":
        cost = MENU["cappuccino"]["cost"]
    else:
        cost = MENU["espresso"]["cost"]

    if cash >= cost:
        change = cash - cost
        m += cost  # Update the total money
        print(f"Your change is {change}")
        return True
    else:
        print("Sorry, not enough money")
        return False


def make_coffee(coffee, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {coffee} ☕️. Enjoy!")
    global order
    order = True

money = 0
order = True
while order:
    print("Hello Customer! ")
    choice = input("What would you like to have, espresso, latte, or cappuccino? ").lower()
    if choice == "off":
        break
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money}")
    else:
        drink = MENU.get(choice)
        if drink:
            if check_resources(choice):
                print("Please enter coins")
                # quarters = $0.25, dimes = $0.10, nickels = $0.05, pennies = $0.01
                total = int(input("how many quarters?: ")) * 0.25
                total += int(input("how many dimes?: ")) * 0.1
                total += int(input("how many nickels?: ")) * 0.05
                total += int(input("how many pennies?: ")) * 0.01
                if check_money(choice, total, money) is not False:
                    money += total
                    make_coffee(choice, drink["ingredients"])
                else:
                    order = False
            else:
                print("Vending Machine needs maintenance ")
                break
        else:
            print("Invalid choice. Please select from espresso, latte, or cappuccino.")


