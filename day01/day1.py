#prompt is "endless gif"


from turtle import *
import turtle
import random

size =100
n=2
turtle.bgcolor("black")
turtle.hideturtle()
turtle.width(3)
turtle.speed(10)
turtle.color("limegreen")
turtle.penup()
turtle.goto(-300,350)
turtle.write("INCOMING ALIEN TRANSMISSION", font=("Courier New", 30, "normal"))


for y in range(200,-200,-size):
    for x in range(-300,300,size):
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