from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("green")
        self.shapesize(stretch_wid=0.5,stretch_len=0.5)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        x_value = random.randint(-290, 280)
        y_value = random.randint(-280, 270)
        self.goto(x=x_value, y=y_value)
