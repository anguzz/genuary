import turtle
import random
#prompt is tessellation 
t = turtle.Screen()
t.tracer(0)
t.bgcolor("#c4faf8")

s_size = 25
s = turtle.Turtle()
s.speed(10)
s.pu()
s.goto(-turtle.window_width()/2,turtle.window_height()/2)
s.pd()

listcolors=['#ffb5e8','#b28dff','#ace7ff','#6eb5ff','#bffcc6','#ffabab','#fff5ba']

a = 0
b = 0
for i in range(100):
    if(b == 0):
        a=1
    else:
        a=0
    for j in range(100):
        s.penup()
        s.hideturtle()
        s.goto(-turtle.window_width() / 2 + j * s_size, (-turtle.window_height() / 2) + i * s_size + s_size)
        s.pendown()
        if(a==0):
            s.fillcolor(random.choice(listcolors))
            a=1
        else:
            s.fillcolor(random.choice(listcolors))
            a=0
        s.begin_fill()
        for k in range(9): 
            s.forward(s_size)
            s.right(60)
        s.end_fill() 
    if(b==0):
        b=1
    else:
        b=0
t.tracer(1)
t.exitonclick()