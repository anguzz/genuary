import turtle
import random

# Set the number of lines to draw and the distance between lines
lines = 11
distance = 50

turtle.width(10)
turtle.color("green")
turtle.bgcolor("#18191B")
turtle.hideturtle()
turtle.speed(0)
turtle.speed('fastest')

# Calculate the width of the bounding area
bounding_width = lines * distance + (lines - 1) * distance

# Move the turtle to the starting position
turtle.penup()
turtle.goto((distance*3), distance*6) 
turtle.pendown()

# Draw the lines
for i in range(lines):
    if i == 8:  # Color the ith row red
        turtle.pencolor('red')
    for j in range(lines):
        turtle.forward(random.randint(-distance, 10))
        turtle.penup()
        turtle.forward(random.randint(-distance, 10))
        turtle.pendown()
    turtle.penup()
    turtle.goto((bounding_width/6), -(i-5)*distance) #changes pos of code draw
    turtle.pendown()


turtle.penup()
turtle.goto(-300,-300)
turtle.write("Error line 8, missing 1 arg", font=("Consolas", 18, "normal"))
# Keep the window open until it is closed
turtle.exitonclick()