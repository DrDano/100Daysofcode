# TODO import data
from data import MENU, resources
# TODO prompt user to choose a drink (What would you like? (espresso/latte/cappuccino):)
# TODO create failsafe for user invalid input
print(f"Menu ~ Espresso: ${MENU['espresso']['cost']}0, Latte: ${MENU['latte']['cost']}0 Cappuccino: ${MENU['cappuccino']['cost']}0 ~")
user_prompt = input("What would you like? (espresso/latte/cappuccino): ")

# TODO prompt user to insert coins
print("Insert Coins")

# TODO create inputs for quarters, dimes, nickels, pennies
quarters = int(input("How many quarters?: "))
dimes = int(input("How many dimes?: "))
nickels = int(input("How many nickels?: "))
pennies = int(input("How many pennies?: "))

# TODO create failsafe for if user invalid input
if quarters or dimes or nickels or pennies is not type(int):
    print("invalid input")

# TODO Create function which adds up all funds
total_funds = quarters*25 + dimes*10 + nickels*5 + pennies
fund_cats = [{"quarters": quarters}, {"dimes": dimes}, {"nickels": nickels}, {"pennies": pennies}]
print(f"You have ${round(total_funds/100,2)} to spend")
print(fund_cats)

# TODO calculate and display change if any
item_cost = MENU[user_prompt]["cost"]
total_change = total_funds - item_cost

def change_calc():
    """takes the remainder of the total change after dividing by each form of currency and returns quantity of 'quarters', 'dimes', etc."""
    change_rem = total_change % 25
    quar_num = total_change / 25
    dime_num = change_rem / 10
    change_rem % 10
    nickel_num = change_rem / 5
    change_rem % 5
    penny_num = change_rem / 1
    change_rem % 1
    return quar_num, dime_num, nickel_num, penny_num

change_calc()
# TODO determine if coffee machine has enough supplies for drink and refund user money if not

change_cats = [{"quarters": change_calc()[0]}, {"dimes": change_calc()[1]}, {"nickelsc": change_calc()[2]}, {"pennies": change_calc()[3]}]
print(change_cats)
# TODO present drink to user and subtract supplies and cost while adding profits
# TODO create function to report resources
# TODO create function to turn off machine
