#day6 genuary prompt is "Steal Like An Artist" 
#art generates on click in the style of Mondrian Art  
import turtle
import random

worldsize=1000
llx=-worldsize
lly=-worldsize
urx=worldsize
ury=worldsize

turtle.hideturtle()
turtle.bgcolor('white')
turtle.setworldcoordinates(llx,lly,urx,ury)
turtle.speed(0)

size=random.randint(3000,5000)
rectangles = random.randint(5,15) 
t = turtle.Turtle()
t.speed(0)
t.hideturtle()

#======border dimensions=============================
num_x_borders =random.randint(2,4)
num_y_borders =random.randint(2,4)
b = turtle.Turtle()
b.hideturtle()
b.speed(0)
horzWidth=random.randint(5,35)
vertWidth=random.randint(5,35)
def drawColorBox(t,random_w, random_h):
    t.hideturtle()
    t.color('white')
    t.fillcolor(random.choice(('red','blue','yellow','white','red','blue','yellow',)))
    t.goto(random.randint(-worldsize,worldsize),random.randint(-worldsize,worldsize))
    t.begin_fill()
    for box in range(2):
        t.left(90)
        t.forward(random_w)
        t.left(90)
        t.forward(random_h)
    t.end_fill()
    t.penup()
    
def drawHorz():
  b.width(horzWidth)
  b.penup()
  b.setx(-200000)
  b.sety(random.randint(-worldsize,worldsize))
  b.pendown()
  b.forward(100000000)


def drawVert():
  b.penup()
  b.width(vertWidth)
  b.setx(random.randint(-worldsize, worldsize))
  b.sety(200000)
  b.pendown()
  heading = b.heading()
  b.right(90)
  b.forward(100000000)
  b.setheading(heading)


def paint(dummy_x=0, dummy_y=0):
    turtle.hideturtle()
    turtle.clearscreen()
    for i in range(rectangles):
        drawColorBox(t,random.randint(10, size),random.randint(10, size))
        turtle.hideturtle()
    turtle.penup()
    for i in range(num_x_borders):
        drawHorz()
        turtle.hideturtle()

    for i in range(num_x_borders):
        drawVert()
        turtle.hideturtle()

    turtle.onscreenclick(paint)
    turtle.hideturtle()

paint()
turtle.listen()
turtle.mainloop()
