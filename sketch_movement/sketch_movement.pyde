keys_pressed = [False for key_code in range(256)]
x, y = 400, 550
pause = False
def setup():
    global pause
    size(800, 700)
    frameRate(60)
    noStroke()

def draw():
    global x, y
    background(0, 255, 0)
    
    if keys_pressed[87]:
        y -= 5
    if keys_pressed[83]:
        y += 5
    if keys_pressed[65]:
        x -= 5
    if keys_pressed[68]:
        x += 5
    
    rectMode(CENTER)
    fill(255, 0, 0)
    rect(constrain(x, 25, 775), constrain(y, 25, 675), 50, 50)
    
def keyPressed():
    global keys_pressed, pause
    print(keyCode)
    keys_pressed[keyCode] = True
    
def keyReleased():
    global keys_pressed, pause
    keys_pressed[keyCode] = False
