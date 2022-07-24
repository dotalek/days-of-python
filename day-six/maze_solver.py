"""
Reeborg's World Maze level challenge solution

The code contained here is meant to work only within the game and by itself will result
in multiple import errors if attempted to run by itself. I've included an import file
to get rid of these errors, but the code will not do anything by itself unless used to
solve the Maze problem over at: https://reeborg.ca/reeborg.html?lang=en&mode=python
"""

from reeborg_actions import move, turn_left, at_goal, front_is_clear, right_is_clear

def turn_right():
    """Turns Reeborg to the right"""
    turn_left()
    turn_left()
    turn_left()

# Make sure we begin next to a wall
while front_is_clear():
    move()
turn_left()

# Find the goal
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
