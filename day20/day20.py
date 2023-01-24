#prompt is art deco 
#draw empire state building 


import turtle
from turtle import *
import random



#draw background sky gradient
#============================================
turtle.title("city night")
turtle.hideturtle()
color = (0.027, .03, 0.094)  # (154, 0, 254)
target = (0, .3, 0.8)  # (221, 122, 80)

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

#draw city skyline

#create a screen object
screen=turtle.Screen()
city=turtle.Turtle()
city.speed(0)
city.hideturtle()
city.penup()
city.setpos(-420,-200)
city.pendown()
a=0
screen.colormode(255)
#We are creating 30 buildings of diffrent sizes using random module
for i in range(1,31):
 x=random.randint(200,300)
 y=random.randint(20,40)
 city.left(90)
 r=random.randint(75,200)
 city.fillcolor(r,r,r)
 city.begin_fill()
 for j in range(1,5):
  if j%2==1:
   city.forward(x)
  else:
   city.forward(y)
  city.right(90)
 city.right(90)
 city.end_fill()
 city.penup()
 city.forward(y)
 a=city.xcor()
 city.forward(random.randint(0,5))
 city.pendown()
city.penup()
city.setpos(-400,-202)
city.pendown()

city.fillcolor('#1F5673')
city.begin_fill()
city.right(90)
city.forward(200)
city.left(90)
city.forward(a+500)
city.left(90)
city.forward(200)
city.end_fill()

#turtle.exitonclick()


#================draw foreground==============
t = turtle.Turtle()
t.speed(6)
myscreen = turtle.Screen()

myscreen.bgcolor("#000324")

t.color("#087CA7")


def draw(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    
#movefunction
def move(len1,angle1,len2,angle2):
    t.hideturtle()
    t.speed(0)
    t.forward(len1)
    t.right(angle1)
    t.forward(len2)
    t.left(angle2)
    
    
draw(-200,-110)
t.begin_fill()
t.forward(410)
t.right(90)
t.forward(100)
t.right(90)
t.forward(410)
t.right(90)
t.forward(100)
t.end_fill()
t.penup

#building 1
t.color("#087CA7")
t.begin_fill()
move(40,90,10,90)
t.forward(20)
t.right(90)
move(30,90,10,90)
move(10,90,10,90)
t.forward(10)

#building 2
t.left(90)
t.forward(20)
t.right(90)
move(20,90,20,90)
t.forward(10)
t.left(90)

#building 3 
t.forward(30)
t.right(90)
t.forward(4)
t.circle(3)
move(4,90,4,90)



#building 4
move(5,90,2,90)
t.forward(5)
t.left(90)
move(7,90,10,90)
move(10,90,6,90)
move(20,90,3,90)
move(10,90,3,90)
t.forward(5)
t.right(90)
move(10,90,5,90)
move(3,90,10,90)
move(3,90,20,90)
move(6,90,20,90)
move(3,90,5,90)
move(4,90,8,90)

#building 5
t.forward(7)
t.left(90)
move(9,90,10,90)

#Empire State 
move(10,90,10,90)
move(100,90,5,90)
move(20,90,5,90)
move(15,90,2,90)
move(10,90,10,90)


# empire state tip 
move(10,90,20,95)
move(90,190,89,95)
move(20,90,10,90)
move(10,90,10,90)
move(2,90,15,90)
move(5,90,20,90)
move(5,90,142,90)

#building 6
t.forward(4)
t.left(90)
t.forward(90)
t.right(90)
move(50,90,4,90)
t.forward(6)
t.right(90)
t.goto(125,-20)

#Chrysler building
t.left(90)
t.forward(20)
t.left(90)
move(12,90,4,90)
t.forward(12)
t.right(90)
t.forward(4)
t.goto(160,30)
t.left(88)
t.forward(20)
t.left(183)
t.forward(20)
t.goto(160,30)
t.left(0)
t.forward(25)
t.left(90)
move(4,90,12,90)
move(4,90,15,90)
move(4,90,60,90)
t.forward(4)
t.left(90)
t.forward(40)
t.right(90)
move(10,90,10,90)
t.forward(15)
t.right(90)
t.forward(60)
t.end_fill()

draw(-200,140)



turtle.exitonclick()