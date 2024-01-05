from turtle import *

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.s = 0
        self.hideturtle()
        self.goto(0,280)
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Score = {self.s}", align="center", font=('Arial', 10, 'normal'))

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER!", align="center", font=('Arial', 10, 'normal'))

    def update_score(self):
        self.s = self.s + 1
        self.write_score()





