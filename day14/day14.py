#prompt is "Aesemic writing"
from turtle import *
import turtle
import random

#============================================

turtle.title("secret scroll ")
turtle.hideturtle()
color = (0, .3, .8)  # (154, 0, 254)
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
#============================================


size =100
n=2

l=800
h=500

startx=-400
starty=-200

t=turtle.Turtle()
t.color("#ad886e")
t.hideturtle()
t.width(3)
t.speed(0)
#draw rect
t.fillcolor('#f8d38b')
t.begin_fill()
t.penup()
t.goto(startx,starty)
t.pendown()
t.forward(l) 
t.left(90) 
t.forward(h) 
t.left(90) 
t.forward(l) 
t.left(90) 
t.forward(h) 
t.left(90)
t.end_fill()

#draw lines
t.penup()
t.goto(startx+40,starty)
t.pendown()
t.forward(40)
t.left(90) 
t.forward(h)
t.pendown()

t.penup()
t.goto(startx+710,starty)
t.pendown()
t.forward(h)
t.pendown()


#draw letters 
turtle.width(4)
turtle.speed(0)
turtle.hideturtle()
turtle.color("black")
for y in range(200,-200,-size):
    for x in range(-280,300,size):
        px=x+random.uniform(-size/4,size/4)
        py=y+random.uniform(-size/4,size/4)
        px_start=px
        py_start=py
        penup()
        goto(px_start,py_start)
        pendown()

        for i in range(n):
            px_end = x + random.uniform(-size/4,size/4)
            py_end = y + random.uniform(-size/4,size/4)
            goto(px_end, py_end)
            px_start=px_end
            py_start=py_end

    goto(px,py)
    language_randomizer = random.randrange(3)
    n+=language_randomizer
end_fill()
done()


turtle.exitonclick()