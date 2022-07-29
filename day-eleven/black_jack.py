"""Blackjack CLI Game

This script allows the user to play a game of Blackjack against an automated dealer.

Special considerations about this version of Blackjack are:
- The deck is of unlimited size.
- There are no suits.
- There are no jokers.
- The Jack, Queen & King all have a value of 10.
- The Ace can count as 11 or 1.
- Cards are not removed from the deck as they are drawn.
- The Dealer hits until it reaches 17 or higher.
"""

import random
import sys

LOGO = r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
ACE = 11
BLACKJACK = 21
DEALER_GOAL = 17


def ask_to_play() -> bool:
    """Asks the user if they want to play a game.

    Return
    ------
    choice : bool
    """
    choice = None
    while True:
        try:
            if (
                input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
                == "n"
            ):
                choice = False
            else:
                choice = True
            break
        except:
            print("That's not a valid option, please type 'y' or 'n': ")
    return choice


def clear() -> None:
    """Clears the terminal window.

    Return
    ------
    None
    """
    print("\033c")
    return


def title_screen() -> None:
    """Clears the screen and prints the program's logo

    Return
    ------
    None
    """
    clear()
    print(LOGO)
    return


def deal_card() -> list[int]:
    """Gets a random card from the deck

    Return
    ------
    list[int]
    """
    deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return [random.choice(deck)]


def calculate_score(hand: list[int]) -> int:
    """Returns the sum of a given hand.

    It takes into account if the hand has an Ace and prevents it from busting.

    Parameters
    ----------
    hand : list[int]
        The given hand to calculate the score for.

    Return
    ------
    score : int
    """
    score = sum(hand)
    while ACE in hand and is_bust(score):
        hand = swap_ace(hand)
        score = calculate_score(hand)
    return score


def swap_ace(hand: list[int]) -> list[int]:
    swapped_hand = hand
    if ACE in swapped_hand:
        ace_index = swapped_hand.index(ACE)
        swapped_hand[ace_index] = 1
    return swapped_hand


def init_hand() -> list[int]:
    """Deals an initial hand to a player.

    Return
    ------
    hand : list[int]
    """
    hand: list[int] = [] + deal_card() + deal_card()
    return hand


def print_hand(hand: list[int]) -> None:
    """Prints a given hand as if it were a player's, and its equivalent total.

    Parameters
    ----------
    hand : list[int]
        The hand to be printed.

    Return
    ------
    None
    """
    score = calculate_score(hand)
    print(f"Your hand {hand}, current score: {score}")
    return


def print_dealer(hand: list[int]) -> None:
    """Prints a given hand as if it were a dealer's; just the first card.

    Parameters
    ----------
    hand : list[int]
        The hand to be printed.

    Return
    ------
    None
    """
    print(f"Dealer's first card: {hand[0]}")
    return


def is_bust(score: int) -> bool:
    """Checks whether a given score has gone past the Blackjack score.

    Parameters
    ----------
    score : int
        The given score to evaluate

    Return
    ------
    bool
    """
    return score > BLACKJACK


def player_turn(hand: list[int]) -> None:
    score = calculate_score(hand)
    if score == BLACKJACK:
        print("Blackjack!")
        return
    while input("Type 'y' to hit, or 'n' to stay: ") != "n":
        hand += deal_card()
        print_hand(hand)
        score = calculate_score(hand)
        if is_bust(score):
            break
    return


def dealer_turn(hand: list[int]) -> None:
    score = calculate_score(hand)
    if score == BLACKJACK:
        return
    while score < DEALER_GOAL:
        hand += deal_card()
        score = calculate_score(hand)
    return


def game_over(player_hand: list[int], dealer_hand: list[int]) -> None:
    player_score = calculate_score(player_hand)
    dealer_score = calculate_score(dealer_hand)
    player_busted = is_bust(player_score)
    dealer_busted = is_bust(dealer_score)
    print(f"Your final hand: {player_hand}, final score: {player_score}")
    print(f"Dealer's final hand: {dealer_hand}, final score: {dealer_score}")
    if player_busted or dealer_score > player_score and not dealer_busted:
        print("Dealer wins!")
    elif dealer_busted or player_score > dealer_score and not player_busted:
        print("Player wins!")
    else:
        print("Draw!")
    return


def play_game() -> None:
    while ask_to_play():
        title_screen()
        player_hand = init_hand()
        dealer_hand = init_hand()
        print_hand(player_hand)
        print_dealer(dealer_hand)
        player_turn(player_hand)
        dealer_turn(dealer_hand)
        game_over(player_hand, dealer_hand)


def main():
    try:
        play_game()
        sys.exit()
    except:
        sys.exit()


if __name__ == "__main__":
    main()
