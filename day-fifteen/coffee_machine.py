"""Simulates the function of a coffee machine.
"""

import sys


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
    },
}


MONEY = {
    "pennies": 0.01,
    "nickles": 0.05,
    "dimes": 0.10,
    "quarters": 0.25,
}


def report():
    """Prints a report of the given list of resources.

    Return
    ------
    _ : None
    """
    for ingredient, quantity in resources.items():
        prefix = ""
        suffix = ""
        if ingredient in ("water", "milk"):
            suffix += "ml"
        if ingredient in ("coffee",):
            suffix += "gr"
        if ingredient in ("money",):
            prefix += "$"
        print(f"{str(ingredient).title()}: {prefix}{quantity}{suffix}")
    return


def turn_off():
    """Simulates the machine turning down. Exits the program.

    Return
    ------
    _ : None
    """
    sys.exit()


# TODO - change the values to the function that will called
ADMIN = {
    "report": report,
    "off": turn_off,
}

resources = {
    "water": 300.0,
    "milk": 200.0,
    "coffee": 100.0,
}


def prompt_choice():
    """Prompts the user to pick an item from the menu.

    Return
    ------
    choice : str
        The user's choice.
    """
    menu = [item for item in MENU.keys()]
    admin_options = [item for item in ADMIN.keys()]
    all_options = admin_options + menu
    choice = ""
    try:
        while choice not in all_options:
            choice = input(f'What would you like? ({"/".join(menu)}): ')
    except RecursionError as e:
        print("Too many wrong attempts.", e)
    return choice


def check_resources(recipe: dict[str, float]) -> bool:
    """Checks if a recipe can be fulfilled with the given resources.

    Parameters
    ----------
    recipe : dict[str, float]
        Collection of ingredients and the amount required.
    storage : dict[str, float]
        Collection of resources in a machine.

    Return
    ------
    _ : bool
    """
    try:
        for ingredient in recipe:
            if resources[ingredient] < recipe[ingredient]:
                print(f"Sorry, there's not enough {ingredient}")
                return False
        return True
    except KeyError as e:
        print("An ingredient couldn't be found", e)
        return False


def process_coins() -> float:
    """Process the amount of money inserted into the machine.

    Asks for input for each of the elements in the MONEY dictionary.

    Return
    ------
    _ : float
        The amount of cash the user input
    """
    inserted_cash: dict[str, float] = {kind: float(0) for kind in MONEY}
    for kind in MONEY:
        inserted_cash[kind] = int(input(f"How many {kind}? ")) * MONEY[kind]
    return sum(inserted_cash.values())


def check_transaction(inserted: float, required: float) -> bool:
    """Evaluates wether the inserted amount of cash is enough for the requested drink.

    If the transaction is successful, the money will be added to the given storage. The user should be given change if the amount exceeds the requirement.

    If the transaction is unsuccessful, the user will be refunded and notified.

    Parameters
    ----------
    inserted : float
        Amount of cash inserted into the machine.
    required : float
        Amount of cash required to process the drink.

    Return
    ------
    _ : bool
    """
    if inserted < required:
        print("Sorry, that's not enough money. Money refunded.")
        return False
    change = round(inserted - required, 2)
    print(f"Here's ${change} in change.")
    return True


def serve_drink(drink: str):
    """Process a drink through the machine.

    It will deduct the given materials from the storage and add the required money.

    Parameters
    ----------
    drink : str
        Name of the requested drink.
    storage : dict[str, float]
        The storage to deduct ingredients and add money to.

    Return
    ------
    _ : None
    """
    try:
        req_drink = MENU[drink]
        for ingredient, amount in req_drink["ingredients"].items():
            resources[ingredient] -= amount
        resources.setdefault("money", 0)
        resources["money"] += req_drink["cost"]
    except KeyError as e:
        print("Sorry, something went wrong and I couldn't process your order.", e)
    finally:
        print(f"Here's your {drink}. Enjoy!")


def main():
    try:
        while True:
            choice = prompt_choice()
            if choice in ADMIN:
                ADMIN[choice]()
                continue  # Restart the process
            drink = MENU[choice]
            enough_ingredients = check_resources(drink["ingredients"])
            if not enough_ingredients:
                continue  # Restart the process
            enough_cash = check_transaction(process_coins(), drink["cost"])
            if not enough_cash:
                continue  # Restart the process
            serve_drink(choice)
    finally:
        return


if __name__ == "__main__":
    main()
