import turtle  
from turtle import *

t = turtle.Turtle() 
t.hideturtle()
t.speed(0) 
t.width(2)
t.color("white")
turtle.Screen().bgcolor("lightblue")

for i in range(100):  
    t.left(165) 
    for i in range(5): 
        t.forward(250) 
        t.left(150)
turtle.exitonclick()