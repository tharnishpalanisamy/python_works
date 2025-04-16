from turtle import Turtle,Screen
import random
screen = Screen()

screen.setup(height=400,width=500)
choice = screen.textinput(title="make your bet",prompt="enter the color of the turtle")
print(choice)
y_position = -60
colors = ["red","blue","green","purple","yellow","orange"]
all_turtles = []

for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-240,y=y_position)
    y_position += 30
    all_turtles.append(new_turtle)

game_on = False
if choice :
    game_on = True
while game_on :
    for turtle in all_turtles:
        turtle.forward(random.randint(1, 10))
        if turtle.xcor() > 230 :
            game_on = False
            if turtle.pencolor() == choice :
                print(f"You won ! {turtle.pencolor()} turtle has won the race !")
            else :
                print(f"You lost ! {turtle.pencolor()} turtle has won the race !")
            break









screen.exitonclick()
