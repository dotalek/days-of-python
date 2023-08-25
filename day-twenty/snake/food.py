from random import randint

from turtle import Turtle


LEFT_LIMIT = -280
RIGHT_LIMIT = 280
BOTTOM_LIMIT = -280
TOP_LIMIT = 280


class Food(Turtle):
    def __init__(self):
        super().__init__("circle")
        self.color('blue')
        self.penup()
        self.shapesize(0.5)
        self.speed("fastest")
        self.change_position()

    def __get_new_pos(self):
        return (randint(LEFT_LIMIT, RIGHT_LIMIT), randint(BOTTOM_LIMIT, TOP_LIMIT))

    def change_position(self):
        self.goto(self.__get_new_pos())
