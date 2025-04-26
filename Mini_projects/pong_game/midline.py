from turtle import Turtle


class Line(Turtle):
    def __init__(self):
        super().__init__()
        self.draw_line()

    def draw_line(self):
        self.color("white")
        self.penup()
        self.goto(0, -300)
        for i in range(22):
            self.pendown()
            self.setheading(90)
            self.forward(20)
            self.penup()
            self.forward(20)
