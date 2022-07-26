"""
Program that simulates a silent auction.
"""

import sys
from os import system

LOGO = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

bids = {}

def clear():
    """Clears the console screen."""
    system("clear")

def add_new_bid(name: str, bid: float):
    """Adds a new entry to the bids dictionary

    Parameters
    ----------
    name : str
        The name of the bid's owner
    bid : float
        The amount the bid's owner is bidding.
    """
    bids[name] = round(bid, 2)

def find_winner(auction: dict):
    """Finds and prints the owner of the best bid

    Parameters
    ----------
    auction : dict
        The dictionary containing all the bids
    """
    winner = ""
    max_bid = 0
    for name, bid in auction.items():
        if bid > max_bid:
            winner = name
            max_bid = bid
    print(f"The winner is {winner} with a bid of ${max_bid}")

try:
    clear()
    print(LOGO)
    while True:
        bidder = input("What is your name?: ")
        bidder_amount = float(input("What is your bid?: $"))
        add_new_bid(bidder, bidder_amount)
        if input("Type 'yes' to add another bid, or 'no' to finalize.\n") == 'no':
            break
    find_winner(bids)
    # bid_list = list(bids.values())
    # max_bid = max(bid_list)
    # winner_index = bid_list.index(max_bid)
    # winner = list(bids.keys())[winner_index]
    # print(f"The winner is {winner} with a bid of ${max_bid}")
except KeyboardInterrupt:
    sys.exit()
