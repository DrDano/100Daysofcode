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
print(total_funds)
print(fund_cats)
# TODO calculate and display change if any
item_cost = MENU[user_prompt]["cost"]
total_change = total_funds - item_cost
quartersc = 0
dimesc = 0
nickelsc = 0
penniesc = 0

while total_change > 0:
    if total_change % 25 == 0:
        quartersc = total_change/25
change_cats = [{"quarters": quartersc}, {"dimes": dimesc}, {"nickelsc": nickels}, {"pennies": penniesc}]
print("hi")
# TODO determine if coffee machine has enough supplies for drink and refund user money if not
# TODO present drink to user and subtract supplies while adding profits
# TODO create function to report resources
# TODO create function to turn off machine
