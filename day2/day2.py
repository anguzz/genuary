from turtle import *
import turtle


t=turtle.Turtle()

t.screen.bgcolor("lightblue")


t.width(3)
t.speed(5)
t.color("blue")
t.penup()

#draw G
t.goto(-30,50) 
t.pendown()
t.pensize(10)
t.pencolor("blue")
t.right(180)
t.circle(50,180)
t.left(90)
t.forward(50)
t.goto(-50,0)
t.right(90)
t.forward(50)
t.right(90)
t.forward(30)
t.penup()

#write 23

t.goto(20,-30)
t.write("23", font=("Comic Sans MS", 50, "normal"))

end_fill()
done()