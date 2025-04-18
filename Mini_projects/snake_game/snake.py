import time
from turtle import Turtle,Screen
STARTING_POSITION = [(0,0),(-20,0),(-40,0)]
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:
    def __init__(self):
        self.blocks = []
        self.create_snake()
        self.head = self.blocks[0]
        self.can_turn = True
        
    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_blocks(position)
            
    def add_blocks(self , position):
        new_block = Turtle(shape="square")
        new_block.penup()
        new_block.color("white")
        new_block.goto(position)
        self.blocks.append(new_block)

    def extend(self):
        self.add_blocks(self.blocks[-1].position())

    def move(self):
        for i in range(len(self.blocks) - 1, 0, -1):
            x_value = self.blocks[i - 1].xcor()
            y_value = self.blocks[i - 1].ycor()
            self.blocks[i].goto(x=x_value, y=y_value)
        self.head.forward(20)
        self.can_turn = True

    def up(self):
        if self.head.heading() != DOWN and self.can_turn:
            self.head.setheading(UP)
            self.can_turn = False

    def down(self):
        if self.head.heading() != UP and self.can_turn:
            self.head.setheading(DOWN)
            self.can_turn = False

    def left(self):
        if self.head.heading() != RIGHT and self.can_turn:
            self.head.setheading(LEFT)
            self.can_turn = False

    def right(self):
        if self.head.heading() != LEFT and self.can_turn:
            self.head.setheading(RIGHT)
            self.can_turn = False






