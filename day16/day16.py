#prompt is reflection of a reflection
#run in processing https://processing.org/

def setup():
  size(640, 360, P3D)
  noStroke()
  fill(204)


def draw():
  noStroke()
  background(23,9,72) 
  dirY = (mouseY / float(height) - 0.5) * 2
  dirX = (mouseX / float(width) - 0.5) * 2
  directionalLight(197, 145, 245, -dirX, -dirY, -1) 
  translate(width/2 - 100, height/2, 0) 
  sphere(80)
  translate(200, 0, 0) 
  sphere(80)