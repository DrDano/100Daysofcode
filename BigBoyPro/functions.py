# TODO import data
from data import MENU, resources

serving = True
runs = 0
water = resources["water"]
milk = resources["milk"]
coffee = resources["coffee"]

water_rem = water
milk_rem = milk
coffee_rem = coffee

while serving == True:

    # TODO prompt user to choose a drink (What would you like? (espresso/latte/cappuccino):)
    # TODO create failsafe for user invalid input
    f = open('art')
    logo = f.read()
    print(logo)
    f.close()

    print(f"Menu ~ Espresso: ${MENU['espresso']['cost']}0, Latte: ${MENU['latte']['cost']}0 Cappuccino: ${MENU['cappuccino']['cost']}0 ~")
    user_prompt = input("What would you like? (espresso/latte/cappuccino): ").lower()

    # TODO create function to report resources
    def report(water_rem, milk_rem, coffee_rem):
        if user_prompt == "report":
            print(f"water remaining: {water_rem}\nmilk remaining: {milk_rem}\ncoffee remaining: {coffee_rem}")
    if user_prompt == "report":
        report(water_rem, milk_rem, coffee_rem)

    # TODO create function to turn off machine
    elif user_prompt == "exit":
        pass

    else:
        # TODO prompt user to insert coins
        print("Insert Coins")

        # TODO create inputs for quarters, dimes, nickels, pennies
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickels = int(input("How many nickels?: "))
        pennies = int(input("How many pennies?: "))

        # TODO Create function which adds up all funds
        total_funds = quarters*25 + dimes*10 + nickels*5 + pennies
        fund_cats = [{"quarters": quarters}, {"dimes": dimes}, {"nickels": nickels}, {"pennies": pennies}]

        # TODO calculate and display change if any
        item_cost = MENU[user_prompt]["cost"]
        total_change = total_funds - item_cost * 100
        money = True
        if total_change <= 0:
            print("Sorry, not enough funds to complete transaction.")
            money = False

        def change_calc():
            """takes the remainder of the total change after dividing by each form of currency and returns quantity of 'quarters', 'dimes', etc."""
            change_rem = total_change % 25
            quar_num = int(round(total_change / 25, 0))
            dime_num = int(round(change_rem / 10, 0))
            change_rem % 10
            if change_rem / 5 > 1:
                nickel_num = int(round(change_rem / 5, 0))
            else:
                nickel_num = 0
            change_rem % 5
            penny_num = int(round(change_rem / 1, 0))
            change_rem % 1
            return quar_num, dime_num, nickel_num, penny_num

        # TODO determine if coffee machine has enough supplies for drink and refund user money if not

        supply = True
        if water_rem - MENU[user_prompt]["ingredients"]["water"] > 0:
            water_rem -= MENU[user_prompt]["ingredients"]["water"]
        else:
            supply = False
        if user_prompt == "espresso":
            pass
        elif milk_rem - MENU[user_prompt]["ingredients"]["milk"] > 0:
            milk_rem -= MENU[user_prompt]["ingredients"]["milk"]
        else:
            supply = False
        if coffee_rem - MENU[user_prompt]["ingredients"]["coffee"] > 0:
            coffee_rem -= MENU[user_prompt]["ingredients"]["coffee"]
        else:
            supply = False

        if not supply:
            print("Machine has not enough resources for drink.")
            print(f"You have been refunded ${total_funds / 100}")

        if supply == True and money == True:
            print(f"Here is your {user_prompt}, enjoy!")
            change_cats = [{"quarters": change_calc()[0]}, {"dimes": change_calc()[1]}, {"nickels": change_calc()[2]}, {"pennies": change_calc()[3]}]
            print(f"Your change is: {change_cats[0]['quarters']} Quarters, {change_cats[1]['dimes']} Dimes, {change_cats[2]['nickels']} Nickels, and {change_cats[3]['pennies']} Pennies.")
        else:
            pass

        # TODO present drink to user and subtract supplies and cost while adding profits
        # TODO Ask user if they would like another drink
        print(f"You have ${round(total_change / 100, 2)} being refunded to you.")

        repeat = input("Would you like to order something else? 'y' or 'n': ").lower()
        if repeat == "n":
            serving = False
