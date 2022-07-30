"""
Collection of exercises to improve debugging skills.

Original lines are commented out right above the solution.
"""


def exercise_1() -> None:
    """Exercise #1"""
    number = int(input("Which number do you want to check?"))
    # if number % 2 = 0: <- This is an assignment instead of a comparison
    if number % 2 == 0:
        print("This is an even number.")
    else:
        print("This is an odd number.")


def exercise_2() -> None:
    """Exercise #2"""
    # year = input("Which year do you want to check?") -> input is not converted to int
    year = int(input("Which year do you want to check?"))

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("Leap year.")
            else:
                print("Not leap year.")
        else:
            print("Leap year.")
    else:
        print("Not leap year.")


def exercise_3():
    """Exercise #3"""
    for number in range(1, 101):
        # if number % 3 == 0 or number % 5 == 0: <- Should use 'and' instead of 'or'
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        # if number % 3 == 0: <- Should use 'elif' instead of 'if'
        elif number % 3 == 0:
            print("Fizz")
        # if number % 5 == 0: <- Should use 'elif' instead of 'if'
        elif number % 5 == 0:
            print("Buzz")
        else:
            # print([number]) <- Number is being printed as a list, remove []
            print(number)
