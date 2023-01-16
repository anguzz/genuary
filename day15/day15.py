
from math import sin
from processing import *
# run at https://trinket.io/processing

radius = 100 
r = 10  
t = 0
circle = []

def setup():
    size(600,600)
    
def draw():
    global t, circle
    background(167,187,236)
    translate(width/4,height/2)
    stroke(0)
    ellipse(0,0,2*radius,2*radius)
    
    fill(91,192,235) 
    y = radius*sin(t)
    x = radius*cos(t)
    circle.insert(0,y)
    
    ellipse(x,y,r,r)
    stroke(172, 236, 247)
    
    line(x,y,200,y)
    fill(73,106,129) 
    
    ellipse(200,y,10,10)
    
    if len(circle)>300:
        circle.remove(circle[-1])
    for i,c in enumerate(circle):
        ellipse(200+i,c,5,5)
    t += 0.05

run()