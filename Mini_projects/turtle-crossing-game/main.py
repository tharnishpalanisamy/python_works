import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
cars = CarManager()
score = Scoreboard()
score.update_score()
screen.listen()
screen.onkey(key="Up" , fun=player.go_up)
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_cars()
    cars.move()
    if player.ycor() > 280 :
        player.refresh()
        score.increase_level()
        cars.increase_speed()
    for  car in cars.all_cars :
        if player.distance(car) < 30 :
            player.refresh()
            score.game_over()
            game_is_on = False


screen.exitonclick()



