"""Object oriented approach to a coffee machine.

It implements libraries authored by Angela Yu.
"""
import sys
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def main():
    menu = Menu()
    maker = CoffeeMaker()
    money = MoneyMachine()
    while True:
        # prompt the user for input
        choice = "None"
        while choice not in menu.get_items() + "report/off":
            choice = input(f"What would you like? ({menu.get_items()}) ")
        # handle special cases (off/report)
        if choice == "off":
            break
        if choice == "report":
            maker.report()
            money.report()
            continue
        # if a drink is requested
        requested_drink = menu.find_drink(choice)
        # check enough resources
        if not maker.is_resource_sufficient(requested_drink):
            print("Sorry, there's not enough resources")
        # ask for money and check transaction
        if not money.make_payment(requested_drink.cost):
            continue
        # make the drink
        maker.make_coffee(requested_drink)
    return


if __name__ == "__main__":
    main()
    sys.exit()
