# TODO import data
from data import MENU, resources
# TODO prompt user to choose a drink (What would you like? (espresso/latte/cappuccino):)
# TODO create failsafe for user invalid input
print(f"Menu ~ Espresso: ${MENU['espresso']['cost']}0, Latte: ${MENU['latte']['cost']}0 Cappuccino: ${MENU['cappuccino']['cost']}0 ~")
user_prompt = input("What would you like? (espresso/latte/cappuccino): ")
# TODO prompt user to insert coins
print("Insert Coins")
# TODO create inputs for quarters, dimes, nickels, pennies
# TODO create failsafe for if user invalid input
quarters = int(input("How many quarters?: "))
dimes = int(input("How many dimes?: "))
nickels = int(input("How many nickels?: "))
pennies = int(input("How many pennies?: "))
# TODO Create function which adds up all funds
# TODO calculate and display change if any
# TODO determine if coffee machine has enough supplies for drink and refund user money if not
# TODO present drink to user and subtract supplies while adding profits
# TODO create function to report resources
# TODO create function to turn off machine
