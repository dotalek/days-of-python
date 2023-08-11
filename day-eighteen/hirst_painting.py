from turtle import Turtle, mainloop, Screen


import random


DIRECTIONS = [0, 90, 180, 270]


def main():
    cursor = Turtle()
    screen = Screen()
    screen.colormode(255)

    # Challenge 1
    def draw_square(size):
        for _ in range(4):
            cursor.right(90)
            cursor.forward(size)
    # draw_square(100)

    # Challenge 2
    def dotted_line(distance):
        for i in range(0, distance, 5):
            if i % 2 == 0:
                cursor.pendown()
            else:
                cursor.penup()
            cursor.forward(5)
    # dotted_line(100)

    # Challenge 3
    def draw_shape(sides):
        angle = 360 / sides
        for _ in range(sides):
            cursor.forward(100)
            cursor.right(angle)

    def overlapped_shapes():
        for sides in range(3, 11):
            cursor.color(random_rgb())
            draw_shape(sides)
    # overlapped_shapes()

    # Challenge 4
    def random_rgb():
        return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def random_walk():
        cursor.shape("circle")
        cursor.shapesize(0.1)
        cursor.speed("fastest")
        cursor.pensize(10)
        for _ in range(200):
            cursor.setheading(random.choice(DIRECTIONS))
            cursor.color(random_rgb())
            cursor.forward(25)
    # random_walk()

    # Challenge 5
    def draw_spirograph(steps, size):
        cursor.speed("fastest")
        angle = 360 / steps
        for i in range(steps):
            cursor.color(random_rgb())
            cursor.circle(size)
            cursor.setheading(angle * (i + 1))
    # draw_spirograph(20, 100)

    mainloop()


if __name__ == "__main__":
    main()
