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

RESOURCES = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
MONEY_EARNED = 0
def printReport(stock, profit):
    print(f"Water: {stock["water"]}\nMilk: {stock["milk"]}\nCoffee: {stock["coffee"]}\nMoney: ${profit}")

def precessCoins(drink):
    print("Please insert coins.")
    quarters = float(input("How many quarters?: "))
    dimes = float(input("How many dimes?: "))
    nickels = float(input("How many nickels?: "))
    pennies = float(input("How many pennies?: "))
    total_money = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
    if float(MENU[drink]["cost"]) > total_money:
        return 0
    else:
        return total_money

def checkResources(drink, stock):
    if stock["water"] >= MENU[drink]["ingredients"]["water"]:
        if stock["coffee"] >= MENU[drink]["ingredients"]["coffee"]:
            if drink == "latte" or drink == "cappuccino":
                if stock["milk"] >= MENU[drink]["ingredients"]["milk"]:
                    stock["water"] = stock["water"] - MENU[drink]["ingredients"]["water"]
                    stock["coffee"] = stock["coffee"] - MENU[drink]["ingredients"]["coffee"]
                    stock["milk"] = stock["milk"] - MENU[drink]["ingredients"]["milk"]
                    return ""
                else:
                    return f"Sorry there is not enough milk"
            else:
                stock["water"] = stock["water"] - MENU[drink]["ingredients"]["water"]
                stock["coffee"] = stock["coffee"] - MENU[drink]["ingredients"]["coffee"]
                return ""
        else:
            return f"Sorry there is not enough coffee"
    else:
        return f"Sorry there is not enough water"


machine_is_on = True
while machine_is_on:
    user_input = input("What would you like? (espresso/latte/cappuccino): ")
    if user_input == "report":
        printReport(RESOURCES, MONEY_EARNED)
    elif user_input in MENU:
        return_money = precessCoins(user_input)
        if return_money == 0:
            print("Sorry, that's not enough money. Money refunded")
        else:
            return_msg = checkResources(user_input, RESOURCES)
            if return_msg == "":
                money_left = return_money - float(MENU[user_input]["cost"])
                MONEY_EARNED += float(MENU[user_input]["cost"])
                print(f"Here is ${round(money_left, 2)} in change. \nHere is your {user_input} Enjoy!")
            else:
                print(return_msg)
    elif user_input == "off":
        machine_is_on = False
    else:
        print("Please check the spelling!!")

