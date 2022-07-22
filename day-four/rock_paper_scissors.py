'''
A CLI Rock, Paper, Scissors game!
'''

import random

rock: str = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper: str = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors: str = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

clear: str = "\033c" # This clears the screen when printed
possible_moves = ['rock', 'paper', 'scissors']
print(clear)
print("Welcome to Rock Paper Scissors")

while True:
    # Grab the inputs from the player and the computer
    print("Choose your move: rock, paper, scissors or quit")
    player_move = input().lower()
    computer_move = random.choice(possible_moves)

    # First check if the player would like to quit
    if player_move[0] == "q":
        break

    # Render the player and computer choices for valid moves
    if player_move in possible_moves:
        print(f"PLAYER USED: {player_move.upper()}")
        if player_move == "rock":
            print(rock)
        elif player_move == "paper":
            print(paper)
        elif player_move == "scissors":
            print(scissors)

        print(f"COMPUTER USED: {computer_move.upper()}")
        if computer_move == "rock":
            print(rock)
        elif computer_move == "paper":
            print(paper)
        elif computer_move == "scissors":
            print(scissors)

        if player_move == computer_move:
            print("DRAW!")
        elif player_move == "rock" and computer_move == "scissors":
            print("PLAYER WINS!")
        elif player_move == "paper" and computer_move == "rock":
            print("PLAYER WINS!")
        elif player_move == "scissors" and computer_move == "paper":
            print("PLAYER WINS!")
        else:
            print("COMPUTER WINS!")

    # Restart the game, invalid choice
    else:
        print("Invalid option, try again.")
        continue

print("Thank you for playing!")
