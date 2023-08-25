import time

from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard


LEFT_LIMIT = -280
RIGHT_LIMIT = 280
BOTTOM_LIMIT = -280
TOP_LIMIT = 280


def main():
    screen: Screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("My Snake Game")
    screen.tracer(0)

    snake = Snake()

    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    food = Food()

    score_config = {
        "size": 16,
    }
    score_config["pos"] = (0, (screen.window_height() -
                               (score_config["size"] * 2.5)) / 2)
    scoreboard = Scoreboard(**score_config)

    game_ongoing = True

    while game_ongoing:
        screen.update()
        time.sleep(0.1)
        snake.move()

        # Handle food collision
        if snake.head.distance(food) <= 15:
            food.change_position()
            snake.add_segment()
            scoreboard.add_point()
            print(snake.segments[1:])

        # Print Scoreboard
        scoreboard.draw_score()

        # Handle wall collision
        if snake.head.xcor() > RIGHT_LIMIT or snake.head.xcor() < LEFT_LIMIT or snake.head.ycor() > TOP_LIMIT or snake.head.ycor() < BOTTOM_LIMIT:
            scoreboard.game_over()
            game_ongoing = False

        # Handle tail collision
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 15:
                game_ongoing = False
    scoreboard.game_over()
    screen.exitonclick()


if __name__ == "__main__":
    main()
