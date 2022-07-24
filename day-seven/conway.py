"""
Conway's Game of Life simulator
"""

import copy
import random
import sys
import time

# Adjust these as you desire
WIDTH = 80
HEIGHT = 21
UPDATE_RATE = 0.2 # Decreasing might result on flickering

def generateBoard(width: int, height: int) -> list[list[int]]:
    """Generates a new random Game of Life board"""
    board: list[list[int]] = []
    for _ in range(height):
        column: list[int] = []
        for _ in range(width):
            column.append(random.randint(0, 1))
        board.append(column)
    return board

def printBoard(board: list[list[int]]) -> None:
    """Prints the game board to the console"""
    print("-" * WIDTH) # Separate the previous board
    for _, row in enumerate(board):
        for _, cell in enumerate(row):
            if cell:
                print("█", end = "") # Live cell
            else:
                print(" ", end = "") # Dead cell
        print() # Row sepparator
    return

def updateLife(board: list[list[int]]) -> list[list[int]]:
    """Applies the game of life rules over a board"""
    newBoard = copy.deepcopy(board)
    for y, row in enumerate(newBoard):
        for x, cell in enumerate(row):
            # Determine neighbor coordinates; left, right, up, down
            left: int = (x - 1) % WIDTH
            right: int = (x + 1) % WIDTH
            up: int = (y - 1) % HEIGHT
            down: int = (y + 1) % HEIGHT

            # Count the living friends
            livingFriends = 0
            if board[up][left]: # Top Left
                livingFriends += 1
            if board[up][x]: # Top
                livingFriends += 1
            if board[up][right]: # Top Right
                livingFriends += 1
            if board[y][right]: # Right
                livingFriends += 1
            if board[down][right]: # Bottom Right
                livingFriends += 1
            if board[down][x]: # Bottom
                livingFriends += 1
            if board[down][left]: # Bottom Left
                livingFriends += 1
            if board[y][left]: # Left
                livingFriends += 1

            # Keep alive or kill the cell
            if (cell and livingFriends in [2, 3]) \
            or (not cell and livingFriends == 3):
                newBoard[y][x] = 1
            else:
                newBoard[y][x] = 0
    return newBoard

# Start simulation
try:
    gameBoard: list[list[int]] = generateBoard(WIDTH, HEIGHT)
    while True:
        printBoard(gameBoard)
        gameBoard = updateLife(gameBoard)
        time.sleep(UPDATE_RATE)
except KeyboardInterrupt:
    sys.exit()
