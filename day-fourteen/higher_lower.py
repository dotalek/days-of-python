"""Play a CLI version of the Higher Lower Game.

The game consists of guessing which celebrity has more followers than the other to score a point. You score a point for each right guess and the game is over once you make a wrong guess. At the end, the game will display the total amount of points collected.

The original can be found at: http://www.higherlowergame.com
"""

from random import randint
from hl_data import DATA, LOGO, VS


def clear() -> None:
    """Clears the terminal window."""
    print("\033c")
    return


def print_logo() -> None:
    """Prints the game's logo."""
    print(LOGO)
    return


def print_title() -> None:
    """Prints the full title screen for the game."""
    clear()
    print_logo()
    return


def get_contenders(contenders) -> list:
    """Gets two different contenders from a dataset"""
    chosen = []
    while len(chosen) < 2:
        current_len = len(contenders)
        chosen.append(contenders.pop(randint(0, current_len)))
    return chosen


def display_contest(cont_1, cont_2) -> None:
    """Prints to the console the contestants and their traits."""
    desc_A = f'Compare A: {cont_1["name"]}, a(n) {cont_1["description"]} from {cont_1["country"]}'
    print(str(cont_1["follower_count"]), desc_A)
    print(VS)
    desc_B = f'Against B: {cont_2["name"]}, a(n) {cont_2["description"]} from {cont_2["country"]}'
    print(str(cont_2["follower_count"]), desc_B)
    return


def ask_guess() -> str:
    """Prompts the user for a guess and returns its value.

    Return
    ------
    guess : str
        The user's guess.
    """
    VALID_RESPONSES = ["A", "B"]
    guess = ""
    while guess not in VALID_RESPONSES:
        guess = input("Who has more followers? Type 'A' or 'B': ")
    return guess


def display_score(score: int) -> None:
    """Prints a given score to the console.

    Parameters
    ----------
    score : int
        The given score to print.
    """
    print(f"You're right! Current score: {score}")
    return


def display_final_score(score: int) -> None:
    """Prints the given score to signals the game over.

    Parameters
    ----------
    score : int
        The given score.
    """
    print(f"Sorry, that's wrong. Final score: {score}")
    return


def play_game() -> None:
    """Play a round of Higher Lower."""
    points = 0
    while True:
        print_title()
        if points > 0:
            display_score(points)
        cont_1, cont_2 = get_contenders(DATA.copy())
        winner = "A"
        if int(cont_2["follower_count"]) > int(cont_1["follower_count"]):
            winner = "B"
        display_contest(cont_1, cont_2)
        guess = ask_guess()
        if guess != winner:
            break
        else:
            print(f"")
            points += 1
    print_title()
    display_final_score(points)


play_game()
