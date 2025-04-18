from turtle import  Screen
import time
from snake import Snake
from food import Food
from score import Score

screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Paambu Game🐍")
screen.tracer(0)
snake = Snake()
food = Food()
score = Score()
screen.listen()
screen.onkey(key="Up",fun=snake.up)
screen.onkey(key="Down",fun=snake.down)
screen.onkey(key="Right",fun=snake.right)
screen.onkey(key="Left",fun=snake.left)
game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    snake.move()
    if snake.head.distance(food) < 15 :
        food.refresh()
        snake.extend()
        score.increase_score()
    if snake.head.xcor() > 280 or snake.head.xcor() < -290 or  snake.head.ycor() > 270 or snake.head.ycor() < -280 :
        game_on = False
        score.game_over()
    for block in snake.blocks[1:]:
        if snake.head.distance(block) < 10:
            game_on = False
            score.game_over()





















screen.exitonclick()
