import turtle
import random
#prompt is signed distance functions


canvas = turtle.Screen()
canvas.setup(width=1000, height=1000)
canvas.bgcolor("black")


t = turtle.Turtle()
t.color("white")
t.hideturtle()
t.speed(0) 
t.penup()
t.setpos(-500, 0)
t.pendown()
t.width(.5)


c = 0  
seen = set()
for s in range(1, 1000):
    back = c - s
    size=3*s/4
    if back > 0 and back not in seen:
        t.setheading(90)
        t.circle(size, 180)
        c = back
        seen.add(c)
    else:
        t.setheading(270) 
        t.circle(size, 180)
        c += s
        seen.add(c)

turtle.done()