#day11 genuary prompt is "suprematism" 
#randomly  generates art on click

  
import turtle
import random
import math

worldsize=1000
llx=-worldsize
lly=-worldsize
urx=worldsize
ury=worldsize

turtle.hideturtle()
turtle.bgcolor('white')
turtle.setworldcoordinates(llx,lly,urx,ury)
turtle.speed(0)

size=random.randint(100,5000)
totalShapes = random.randint(5,15) 
totalLines=random.randint(3,5) 
t = turtle.Turtle()
t.speed(0)
t.hideturtle()
#======border dimensions=============================
num_x_borders =random.randint(1,3)
num_y_borders =random.randint(1,3)
b = turtle.Turtle()
b.hideturtle()
b.speed(0)
horzWidth=random.randint(5,35)
vertWidth=random.randint(5,35)
randWidth=random.randint(5,35)



def drawCircle(box):
    random_r=random.randint(2,5)
    box.color('#ffffff')
    box.fillcolor(random.random(), random.random(), random.random())
    box.goto(random.randint(-worldsize,worldsize),random.randint(-worldsize,worldsize))
    box.begin_fill()
    for i in range(2):
        box.circle(90*random_r)       
    box.end_fill()
    box.penup()


def drawColorBox(t):
    random_w=random.randint(10, size)
    random_h=random.randint(10, size)
    t.hideturtle()
    t.color('#ffffff')
    t.fillcolor(random.random(), random.random(), random.random())
    t.goto(random.randint(-worldsize,worldsize),random.randint(-worldsize,worldsize))
    t.begin_fill()
    for box in range(2):
        t.left(90)
        t.forward(random_w)
        t.left(90)
        t.forward(random_h)
    t.end_fill()
    t.penup()

def drawShape(t):
    random_w=random.randint(10, size)
    random_h=random.randint(10, size)
    t.hideturtle()
    t.color('#ffffff')
    t.fillcolor(random.random(), random.random(), random.random())
    t.goto(random.randint(-worldsize,worldsize),random.randint(-worldsize,worldsize))
    t.begin_fill()
    for box in range(2):
        t.left(random.randint(0,180))
        t.forward(random_w)
        t.left(random.randint(0,180))
        t.forward(random_h)
    t.end_fill()
    t.penup()

def drawHorLines():
  for i in range(totalLines):
    b.width(randWidth)
    b.penup()
    b.setx(-200000)
    b.sety(random.randint(-worldsize,worldsize))
    b.pendown()
    b.forward(100000)
    b.circle(90)
    b.forward(1222)


def drawVertLines():
 for i in range(totalLines):
  b.penup()
  b.width(vertWidth)
  b.setx(random.randint(-worldsize, worldsize))
  b.sety(200000)
  b.pendown()
  heading = b.heading()
  b.right(90)
  b.forward(100000000)
  b.setheading(heading)

def drawRandLines():
    b.speed(0) 
    for i in range(totalLines):
        b.pencolor(random.random(), random.random(), random.random()) 
        b.pendown()
        b.forward(random.randint(1000, 3000)) 
        b.right(random.randint(0, 360)) 
        b.penup()
        b.goto(random.randint(-worldsize,worldsize), random.randint(-worldsize,worldsize)) 



def paint(dummy_x=0, dummy_y=0):
    turtle.hideturtle()
    turtle.clearscreen()
    for i in range(totalShapes):
        drawColorBox(t)
        turtle.hideturtle()
    for i in range(math.ceil(totalShapes/4)): #less circles and other shapes
        drawCircle(t)
        drawShape(t)
        turtle.hideturtle()   
    turtle.penup()
    drawVertLines()
    drawHorLines()
    drawRandLines()
    turtle.hideturtle()
    turtle.onscreenclick(paint)
    turtle.hideturtle()

paint()
turtle.listen()
turtle.mainloop()
