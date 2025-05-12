import time
from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.penup()
        self.hideturtle()
        self.goto(-250, 250)
        self.write(f"Level:{self.level}", font=("Courier", 24, "normal"))

    def increase_level(self):
        self.level += 1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Courier", 36, "bold"))
        self.level = 1










