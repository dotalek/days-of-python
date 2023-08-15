from turtle import Turtle, Screen


DISTANCE = 10
ANGLE = 10


def main():
    screen = Screen()
    cursor = Turtle()

    def move_forward():
        cursor.forward(DISTANCE)

    def move_backward():
        cursor.backward(DISTANCE)

    def rotate_clockwise():
        cursor.right(ANGLE)

    def rotate_cclockwise():
        cursor.left(ANGLE)

    screen.listen()
    screen.onkey(key="w", fun=move_forward)
    screen.onkey(key="s", fun=move_backward)
    screen.onkey(key="a", fun=rotate_cclockwise)
    screen.onkey(key="d", fun=rotate_clockwise)
    screen.onkey(key="c", fun=screen.reset)

    screen.exitonclick()


if __name__ == "__main__":
    main()
