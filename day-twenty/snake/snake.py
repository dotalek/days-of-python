from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self) -> None:
        self.segments: list[Turtle] = self.__init_segments()
        self.head = self.segments[0]

    def __init_segments(self) -> list[Turtle]:
        segments: list[Turtle] = []
        for pos in STARTING_POSITIONS:
            segment = Turtle("square")
            segment.color("white")
            segment.penup()
            segment.goto(pos)
            segments.append(segment)
        return segments

    def move(self) -> None:
        if (len(self.segments) > 0):
            for i in range(len(self.segments) - 1, 0, -1):
                segment = self.segments[i]
                next_segment = self.segments[i - 1]
                (x, y) = next_segment.pos()
                segment.goto((x, y))
            self.head.forward(MOVE_DISTANCE)

    def up(self) -> None:
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self) -> None:
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self) -> None:
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self) -> None:
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
