#prompt is grid inside a grid
#run in processing https://processing.org/
def setup():
    size(800,500,P3D)
    noStroke()


def draw():
    lighting()
    background(100)

    for x in range(0, width, 70):
        for y in range(0, height, 70):
            pushMatrix()
            translate(x,y)
            rotateY(map(mouseX,0,width,0,PI))
            rotateX(map(mouseY,0,height,0,PI))
            box(90)
            popMatrix()

def lighting():
    pointLight(251,98,246, 200,-150,0)#rgb followed by xyz axis
    directionalLight(1,255,79,1,0,0)
    spotLight(26,200,237,   #rgb
            100, 200, 200,      #pos
            0, -0.5, -0.5,   #dir
            PI/2, 2)       #angle
    spotLight(250,229,25,   
            700, 600, 200,      
            0, -0.5, -0.5,   
            PI/2, 2)       
    
