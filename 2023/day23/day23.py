
#prompt is Moiré pattern


import turtle
from turtle import*

delta = 3
min = delta * 3
cursor = 20
lines = 250
screen = Screen()
turtle = Turtle("triangle", visible=False)
turtle.fillcolor("white")

for size in range(((lines - 1) * delta) + min, min - 1, -delta):
    turtle.goto(turtle.xcor() + delta/2, turtle.ycor() - delta/2)
    turtle.shapesize(size / cursor)
    turtle.stamp()

screen.exitonclick()