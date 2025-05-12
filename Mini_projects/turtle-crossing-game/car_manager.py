import random
import time
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE


    def create_cars(self):
        chance = random.randint(1,5)
        if chance == 1 :
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1 , stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.goto(300,random.randint(-250,250))
            self.all_cars.append(new_car)

    def increase_speed(self):
        self.car_speed += 1


    def move(self):
        for car in self.all_cars :
            car.setheading(180)
            car.forward(self.car_speed)
        self.all_cars = [car for car in self.all_cars if car.xcor() > -320]

