from turtle import Turtle
ALIGNMENT = "center"
FONT = ("courier",22,"bold")
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0,270)
        self.color("white")
        self.score = 0
        self.current_score()
    def current_score(self):
        self.write(f"SCORE : {self.score} ",  align=ALIGNMENT , font=FONT)
    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"SCORE : {self.score} ", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over !", align=ALIGNMENT, font=FONT)
