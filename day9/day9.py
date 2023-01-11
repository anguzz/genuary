import turtle
from turtle import *
import random

#prompt is "plants"
petalColor='#f08080'
woodColor='#bea57c'
snowColor='#ffffff'
bgColor='#a8f1d4'

canvas = turtle.Screen()
canvas.setup(width=900, height=1000)
canvas.bgcolor(bgColor)

t = turtle.Turtle()
t.hideturtle() 
t.getscreen().tracer(3, 0)
t.left(90)
t.up()
t.backward(150)
t.down()
t.color(woodColor)


def drawTree(branch, tree):
    if branch > 3:
        if 8 <= branch <= 12:
            if random.randint(0, 2) == 0:
                tree.color(snowColor) 
            else:
                tree.color(petalColor) 
            tree.pensize(branch / 3)
        elif branch < 8:
            if random.randint(0, 1) == 0:
                tree.color(snowColor)
            else:
                tree.color(petalColor)  
            tree.pensize(branch / 2)
        else:
            tree.color(woodColor)  
            tree.pensize(branch / 10)  # 6
        tree.forward(branch)
        a = 2 * random.random()
        tree.right(20 * a)
        b = 2* random.random()
        drawTree(branch - 10 * b, tree)
        tree.left(40 * a)
        drawTree(branch - 10 * b, tree)
        tree.right(20 * a)
        tree.up()
        tree.backward(branch)
        tree.down()


def drawFallenPetals(m, petal):
    for i in range(m):
        a = 200 - 400 * random.random()
        b = 10 - 20 * random.random()
        petal.up()
        petal.forward(b)
        petal.left(90)
        petal.forward(a)
        petal.down()
        petal.color(petalColor) 
        petal.circle(1)
        petal.up()
        petal.backward(a)
        petal.right(90)
        petal.backward(b)



drawTree(90, t)
drawFallenPetals(200, t)
turtle.exitonclick()