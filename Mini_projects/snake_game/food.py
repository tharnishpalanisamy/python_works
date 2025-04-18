from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self , snake ):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("green")
        self.shapesize(stretch_wid=0.5,stretch_len=0.5)
        self.speed("fastest")
        self.refresh()
        self.snake = snake

    def refresh(self):
        while True:
            x_value = random.randint(-270, 270)
            y_value = random.randint(-270, 270)
            self.goto(x=x_value, y=y_value)

            too_close = False
            for block in self.snake.blocks:
                if self.distance(block) < 15 :
                    too_close = True
                    break
            if not too_close :
                break 
