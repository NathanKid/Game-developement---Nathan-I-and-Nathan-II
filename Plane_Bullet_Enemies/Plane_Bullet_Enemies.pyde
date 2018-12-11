x = 0

def setup():
  frameRate(60)
  size(640, 480)

def draw():
  background(0)
  
  #load plane
  plane = loadImage("Plane.gif")
  image(plane, 260, 300)

  #load bullet
  bullet = loadImage("Bullet.png")
  image(bullet, 308, 302)

def mouseClicked():
  print(mouseX, mouseY)
