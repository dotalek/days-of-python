from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self, pos=(0, 0), size=8):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(pos)
        self.size = size
        self.score = 0

    def draw_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score}", move=False,
                   align='center', font=('Arial', self.size, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="Game Over", move=False,
                   align="center", font=("Arial", 20, "normal"))

    def add_point(self):
        self.score += 1
