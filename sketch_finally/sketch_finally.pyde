y = 340 #y-axis of bullet
x = 0 # equivalent of True and False

def setup():
    size(640, 480)
    frameRate(60)
    noStroke()
    
def draw():
    global y, x
    background(0, 255, 0)
    rectMode(CENTER)
    rect(320, 350, 50, 50)
    
    #bullet
    fill(255, 0, 0)
    rect(320, y, 10, 10)
    
    if mousePressed:
        bullet()
    elif not mousePressed and x == 1:
        mousedone()

def bullet():
    global y, x
    y = y - 5
    if y <= 0:
        y = 320
    if x == 0:
        x = 1

def mousedone():
    global y 
    if y > - 1:
        y = y - 5
    
def mouseReleased():
    print(mouseX, mouseY)
