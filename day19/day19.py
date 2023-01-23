import turtle
import random
from turtle import *

#prompt is black and white


#draw background gradient from black to white
turtle.title("yinyang ")
turtle.hideturtle()
color = (0, 0, 0)  # (154, 0, 254)
target = (1, 1, 1)  # (221, 122, 80)

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
#===================================================

win = turtle.Screen() #background color of the window
win.bgcolor("white")
t = turtle.Turtle()
t.speed(0)
t.hideturtle()

#rotate turtle randomly to draw yinyang at random angle
t.right(random.randint(0,360))




#draw outline and white base
t.begin_fill()
t.color("white")
t.right(90)
t.forward(200)
t.left(90)
t.color("white")
t.circle(200)
t.end_fill()
t.color("black")
t.circle(200)

#draw small black circle
t.color("white")
t.left(90)
t.forward(400)
t.color("black")
t.fillcolor("black")
t.begin_fill()
t.left(90)
t.circle(100)
t.end_fill()

#draw half black circle
t.fillcolor("black")
t.begin_fill()
t.left(90)
t.forward(400)
t.left(90)
t.circle(200,180)
t.end_fill()


#draw white half circle
t.left(90)
t.forward(200)
t.color("white")
t.fillcolor("white")
t.begin_fill()
t.right(90)
t.circle(99)
t.end_fill()



#draw white eye inside black area
t.color("black")
t.right(90)
t.forward(75)
t.right(90)
t.fillcolor("white")
t.begin_fill()
t.circle(25)
t.end_fill()

#draw black eye inside white area
t.right(90)
t.forward(75)
t.color("white")
t.forward(75)
t.right(90)
t.fillcolor("black")
t.begin_fill()
t.circle(25)
t.end_fill()

turtle.done()
turtle.exitonclick()