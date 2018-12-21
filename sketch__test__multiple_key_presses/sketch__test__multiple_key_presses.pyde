right_Pressed = False
left_Pressed = False

def setup():
    size(640, 480)
    frameRate(60)

def draw():
    global right_Pressed, left_Pressed
    background(0)
    if right_Pressed:
        ellipse(50, 50, 50, 50)
    
    if left_Pressed:
        ellipse(100, 100, 100, 100)
        
def mousePressed():
    global right_Pressed, left_Pressed
    if mouseButton == LEFT:
        left_Pressed = True
    if mouseButton == RIGHT:
        right_Pressed = True
        
def mouseReleased():
    global right_Pressed, left_Pressed
    if mouseButton == LEFT:
        left_Pressed = False
    if mouseButton == RIGHT:
        right_Pressed = False
