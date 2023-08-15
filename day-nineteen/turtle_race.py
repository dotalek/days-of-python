from turtle import Turtle, Screen


import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
POSITIONS = [i for i in range(-100, 100, int(200 / len(COLORS)))]


def main():
    def get_bet():
        return screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color:").lower()

    def init_turtles(amount=len(COLORS)):
        amount = len(COLORS) if amount > len(COLORS) or amount < 1 else amount
        turtles = []
        for i in range(amount):
            # Create a new turtle
            new_turtle = Turtle()
            new_turtle.penup()
            new_turtle.shape("turtle")
            new_turtle.color(COLORS[i])

            # Move turtle to its initial spot
            new_turtle.goto(x=-230, y=POSITIONS[i])

            turtles.append(new_turtle)
        return turtles

    def goal_reached():
        for turtle in turtles:
            return turtle.xcor() >= 230

    def race():
        goal_reached = False
        winning_turtle = None
        while not goal_reached:
            for turtle in turtles:
                distance = random.randint(1, 10)
                turtle.forward(distance)
                if turtle.xcor() >= 230:
                    goal_reached = True
                    winning_turtle = turtle

        print(f"The winning turtle is {winning_turtle.pencolor()}!")
        return winning_turtle

    screen = Screen()
    screen.setup(width=500, height=400)
    player_bet = get_bet()
    turtles = init_turtles()

    if player_bet in COLORS:
        winner = race()
        if (winner.pencolor() == player_bet):
            print("Congratulations, you won!")
        else:
            print("Better luck next time!")
    else:
        print("Invalid color chosen, unable to race")

    screen.exitonclick()


if __name__ == "__main__":
    main()
