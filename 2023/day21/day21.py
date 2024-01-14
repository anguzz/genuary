import turtle
import random


turtle.speed(0)
turtle.hideturtle()
turtle.bgcolor("black")


def getRandomColor():
	color = "#%06x" % random.randint(0, 0xFFFFFF)
	return color


colorList1=[getRandomColor(),getRandomColor(),getRandomColor(),getRandomColor(),getRandomColor(),getRandomColor()]

lineNum = 1
rowNum = 1
quiltWidth = 800
lineWidth = 2
penColor = ("#333333")


colorCount = 2
patternCount = 5 
blockLen = quiltWidth / lineNum
gap = blockLen/10
turtle.color(penColor)
turtle.width(lineWidth)
beginPos = turtle.pos()
quiltWidth = gap * 5
bgWidth  = blockLen * lineNum + gap * ( lineNum - 1)
bgHeight = blockLen * rowNum + gap * ( rowNum - 1)

turtle.penup()
turtle.setpos(-(blockLen*lineNum+gap*lineNum+quiltWidth*2)/2,(blockLen*rowNum+gap*rowNum+quiltWidth*2)/2)
turtle.setpos(-blockLen/2, blockLen/2)
turtle.pendown()



def drawSq():
    for i in range (0,4):
        turtle.forward(blockLen)
        turtle.right(90)

def drawSquare(length):
    for i in range (0,4):
        turtle.forward(length)
        turtle.right(90)

def gotoBlockCenter(degree, halfsize):
    turtle.penup()
    turtle.forward(blockLen/halfsize)
    turtle.right(90*degree)
    turtle.forward(blockLen/halfsize)
    turtle.pendown()

def moveRightHalfBlock():
    turtle.penup()
    turtle.seth(0)
    turtle.forward(blockLen/2)
    turtle.pendown()

def drawHalfBlock(color):
    turtle.begin_fill ()
    turtle.fillcolor(color)
    drawSquare(blockLen/2)
    turtle.end_fill ()

def gotoBeginPos():
    turtle.penup()
    turtle.goto(beginPos)
    turtle.seth(0)
    turtle.pendown()

def moveit(position):
    turtle.penup()
    turtle.goto(position)
    turtle.pendown()

def moveDivide(divide):
    turtle.penup()
    turtle.forward(blockLen/divide)
    turtle.pendown()

def drawQuilt(color1, color2):
	currentPos = turtle.pos() 
	drawSq() 
	arcRepeat = 4  
	
	def drawArc(color):
		turtle.begin_fill ()
		turtle.fillcolor(color)
		turtle.circle(blockLen/arcRepeat, 360/12)
		turtle.right(360/6)
		turtle.circle(blockLen/arcRepeat, -(360/12))
		turtle.right(360/6)
		turtle.circle(blockLen/arcRepeat, 360/12)
		turtle.end_fill ()

	def drawArcBlock(color):
		for i in range(0,2):
			drawArc(color)
			turtle.right(90)
			drawArc(color)
		gotoBlockCenter(-1,4)

	def drawSubBlock(color):
		turtle.seth(0)
		turtle.begin_fill()
		turtle.fillcolor(color)
		drawSquare(blockLen/arcRepeat)
		turtle.end_fill()

	def goCenter():
		turtle.penup()
		turtle.forward(blockLen/arcRepeat/2)
		turtle.right(90)
		turtle.forward(blockLen/arcRepeat/2)
		turtle.pendown()

	currentColorList = [color1, color2]
	for j in range(0,arcRepeat):
		moveit(currentPos)
		y = turtle.ycor()
		for i in range(0,arcRepeat):
			x = turtle.xcor()
			turtle.pu()
			turtle.goto(x + i * blockLen/arcRepeat, y - j * blockLen/arcRepeat)
			turtle.pd()
			turtle.seth(0)
			drawSubBlock(currentColorList[0 + (i+j+1) % 2])
			goCenter()
			drawArcBlock(currentColorList[0 + (i+j) % 2])
			moveit(currentPos)
		turtle.seth(0)
	gotoBeginPos()
              
colorChoice = colorList1
drawQuilt (colorChoice[0], colorChoice[1])

turtle.exitonclick()

