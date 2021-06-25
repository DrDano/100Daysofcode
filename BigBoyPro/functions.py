# TODO import data
from data import MENU, resources

water = resources["water"]
milk = resources["milk"]
coffee = resources["coffee"]
# TODO prompt user to choose a drink (What would you like? (espresso/latte/cappuccino):)
# TODO create failsafe for user invalid input
print(f"Menu ~ Espresso: ${MENU['espresso']['cost']}0, Latte: ${MENU['latte']['cost']}0 Cappuccino: ${MENU['cappuccino']['cost']}0 ~")
user_prompt = input("What would you like? (espresso/latte/cappuccino): ")

# TODO create function to report resources
def report(water_rem, milk_rem, coffee_rem):
    if user_prompt == "report":
        print(f"water remaining: {water_rem}\nmilk remaining: {milk_rem}\ncoffee remaining: {coffee_rem}")
if user_prompt == "report":
    report(water_rem = water, milk_rem = milk, coffee_rem = coffee)

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
    print(f"You have ${round(total_funds/100,2)} to spend")

    # TODO calculate and display change if any
    item_cost = MENU[user_prompt]["cost"]
    total_change = total_funds - item_cost * 100

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
    if resources["water"] - MENU[user_prompt]["ingredients"]["water"] > 0:
        water -= MENU[user_prompt]["ingredients"]["water"]
    else:
        print("Sorry, not enough resources.")
        print(f"You have ${total_funds/100} to spend.")
        supply = False
    if user_prompt == "espresso":
        pass
    elif resources["milk"] - MENU[user_prompt]["ingredients"]["milk"] > 0:
        milk -= MENU[user_prompt]["ingredients"]["milk"]
    else:
        print("Sorry, not enough resources.")
        print(f"You have ${total_funds/100} to spend.")
        supply = False
    if resources["coffee"] - MENU[user_prompt]["ingredients"]["coffee"] > 0:
        coffee -= MENU[user_prompt]["ingredients"]["coffee"]
    else:
        print("Sorry, not enough resources.")
        print(f"You have ${total_funds/100} to spend.")
        supply = False

    if supply == True:
        print(f"Here is your {user_prompt}, enjoy!")
        change_cats = [{"quarters": change_calc()[0]}, {"dimes": change_calc()[1]}, {"nickelsc": change_calc()[2]}, {"pennies": change_calc()[3]}]
        print(f"Your change is: {change_cats[0],change_cats[1],change_cats[2]}, {change_cats[3]}")

    # TODO present drink to user and subtract supplies and cost while adding profits
