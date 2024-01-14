
import turtle
from turtle import *
#prompt is "something you've always wanted to learn" 

turtle.title("Pokeball")
turtle.hideturtle()
color = (0, 1, 1)  # (154, 0, 254)
target = (0.3843, 0.1490, 0.6588)  # (221, 122, 80)

tur = Screen()
tur.tracer(False)

width, height = tur.window_width(), tur.window_height()
deltas = [(hue - color[index]) / height for index, hue in enumerate(target)]
bg = Turtle()
bg.color(color)
bg.penup()
bg.goto(-width/2, height/2)
bg.pendown()
direct = 1
for distance, y in enumerate(range(height//2, -height//2, -1)):
    bg.forward(width * direct)
    bg.color([color[i] + delta * distance for i, delta in enumerate(deltas)])
    bg.sety(y)
    direct *= -1
tur.tracer(True)

def drawBall(t):
    #red half circle
    t.penup()
    t.forward(30)
    t.pendown()
    t.fillcolor('red')
    t.begin_fill()
    t.forward(60)
    t.left(90)
    t.circle(90,180)
    t.left(90)
    t.forward(60)
    t.end_fill()

    #white outer half circle
    t.penup()
    t.left(90)
    t.left(90)
    t.forward(60)
    t.left(90)
    t.pendown()
    t.fillcolor('white')
    t.begin_fill()
    t.circle(90,180)
    t.end_fill()
    #white inner  circle
    t.penup()
    t.right(90)
    t.forward(-70)
    t.left(110)
    t.pendown()
    t.fillcolor('white')
    t.begin_fill()
    t.circle(20)
    t.end_fill()
    
    



t=turtle.Turtle()
t.hideturtle()
t.speed(0)
t.pensize(12)


drawBall(t)
turtle.exitonclick()