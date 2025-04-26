import time
from turtle import Turtle , Screen
from paddle import Paddle
from ball import Ball
from score import Score
from midline import Line

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("pong")
screen.tracer(0)

r_paddle = Paddle((370,0))
l_paddle = Paddle((-370,0))
ball = Ball()
score = Score()
line = Line()


screen.listen()
screen.onkey(fun=r_paddle.go_up,key="Up")
screen.onkey(fun=r_paddle.go_down,key="Down")
screen.onkey(fun=l_paddle.go_up,key="w")
screen.onkey(fun=l_paddle.go_down,key="s")


game_on = True
while game_on:
    time.sleep(0.07)
    screen.update()
    ball.move()
    if ball.ycor() > 270 or ball.ycor() < -270 :
        ball.y_bounce()
    if ball.xcor() > 340 and ball.distance(r_paddle) < 50:
        ball.goto(340, ball.ycor())
        ball.x_bounce()
    if ball.xcor() < -340 and ball.distance(l_paddle) < 50:
        ball.goto(-340, ball.ycor())
        ball.x_bounce()
    if ball.xcor() > 380 :
        score.l_increase()
        ball.refresh()
    if ball.xcor() < -380 :
        score.r_increase()
        ball.refresh()



screen.exitonclick()
