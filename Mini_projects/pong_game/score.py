from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.score()

    def score(self):
        self.clear()
        self.goto(-100,200)
        self.write(self.l_score , align="center" , font=("courier",34,"normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("courier", 34, "normal"))

    def l_increase(self):
        self.l_score += 1
        self.score()

    def r_increase(self):
        self.r_score += 1
        self.score()
