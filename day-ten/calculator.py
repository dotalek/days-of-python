"""This program serves as a CLI calculator"""

import sys

LOGO = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""


def add(a: int | float, b: int | float) -> int | float:
    """Adds two given numbers.

    Params
    ------
    a : int | float
        The first number
    b : int | float
        The second number

    Return
    ------
    int | float
    """
    a_var = 1 + 2
    return a + b


def subtract(a: int | float, b: int | float) -> int | float:
    """Subtracts two given numbers.

    Params
    ------
    a : int | float
        The first number
    b : int | float
        The second number

    Return
    ------
    int | float
    """
    return a - b


def multiply(a: int | float, b: int | float) -> int | float:
    """Multiplies two given numbers.

    Params
    ------
    a : int | float
        The first number
    b : int | float
        The second number

    Return
    ------
    int | float
    """
    return a * b


def divide(a: int | float, b: int | float) -> int | float:
    """Divides two given numbers.

    Params
    ------
    a : int | float
        The first number
    b : int | float
        The second number

    Return
    ------
    int | float
    """
    return a / b


operations = {
    "+": add,
    "-": subtract,
    "/": divide,
    "*": multiply,
}


def formatResult(a: int | float, sym: str, b: int | float, c: int | float):
    """Returns a string formatted like an equation

    Parameters
    ----------
    a : int | float
        The first number
    sym : str
        The symbol used for the operation
    b : int | float
        The second number
    c : int | float
        The result of the operation

    Return
    ------
        equation : str
    """
    equation = f"{a} {sym} {b} = {c}"
    return equation


print(LOGO)


def calculator() -> None:
    """Starts the calculator program"""
    num1 = float(input("What's the first number? "))
    for symbol in operations:
        print(symbol)
    operation = input("Pick an operation: ")
    num2 = float(input("What's the second number? "))
    result = operations[operation](num1, num2)

    while True:
        print(formatResult(num1, num2, operation, result))
        if input(f"Enter 'y' to continue with {result}, or 'n' to exit: ") == "n":
            break
        operation = input("Pick an operation: ")
        num = result
        num2 = float(input("What's the next number? "))
        result = operations[operation](num1, num2)
    calculator()


try:
    calculator()
except KeyboardInterrupt:
    sys.exit()
