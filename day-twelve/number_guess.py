"""CLI Implementation of Guess the Number Game

Depending on difficulty, the player gets more or less attempts at figuring out the number.
"""

import random
import sys


LOGO = r"""
                                                                              
,---.                        --.--|             ,   .          |              
|  _..   .,---.,---.,---.      |  |---.,---.    |\  |.   .,-.-.|---.,---.,---.
|   ||   ||---'`---.`---.      |  |   ||---'    | \ ||   || | ||   ||---'|    
`---'`---'`---'`---'`---'      `  `   '`---'    `  `'`---'` ' '`---'`---'`    
                                                                              
"""
DIFFICULTIES = {"easy": 10, "hard": 5}
LOWEST = 1
HIGHEST = 100


def title_screen() -> None:
    """Print the game's logo and welcome the player."""
    print(LOGO)
    print("Welcome to The Number Guessing Game!")
    print("I'm thinking of a number between {LOWEST} and {HIGHEST}")
    return


def ask_difficulty() -> str:
    """Prompts the user for a valid difficulty.

    Return
    ------
    user_input : str
    """
    difficulties = [name for name in DIFFICULTIES.copy()]
    diff_str = ", ".join(difficulties)
    user_input = ""
    while user_input not in difficulties:
        user_input = str(input(f"Choose a difficulty. Type {diff_str}: "))
    return user_input


def set_difficulty(difficulty: str) -> int:
    """Returns the amount of tries for a given difficulty.

    Difficulties are specified in a constant dictionary.

    Parameters
    ----------
    difficulty : str
        The given difficulty

    Return
    ------
    tries : int
    """
    tries = 1
    if difficulty in DIFFICULTIES:
        tries = DIFFICULTIES[difficulty]
    return tries


def take_guess() -> int:
    """Prompts the user to take a guess.

    Return
    ------
    guess : int
    """
    guess = int(input("Make a guess: "))
    return guess


def game_loop() -> None:
    """Starts a round of the game."""
    difficulty = ask_difficulty()
    attempts = set_difficulty(difficulty)
    secret_num = random.randint(LOWEST, HIGHEST)
    while attempts > 0:
        print(f"You have {attempts} remaining to guess the number.")
        guess = take_guess()
        if guess == secret_num:
            break
        elif guess > secret_num:
            print("Too high.")
        elif guess < secret_num:
            print("Too low.")
        print("Guess again.")
        attempts -= 1
    if attempts > 0:
        print("You got it!, the answer was 79")
    else:
        print("You've run out of guesses you loose.")
    return


def main() -> None:
    """The main program loop."""
    title_screen()
    game_loop()
    return


if __name__ == "__main__":
    try:
        main()
    except:
        sys.exit()
