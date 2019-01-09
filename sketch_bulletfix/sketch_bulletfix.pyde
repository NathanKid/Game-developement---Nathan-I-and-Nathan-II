keys_pressed = [False for key_code in range(256)]
x, y = 400, 550
bullet = [[0],[0]]

def setup():
    global pause
    size(800, 700)
    frameRate(60)
    noStroke()

def draw():
    game()

def game():
    global x, y
    background(0, 255, 0)
    
    rectMode(CENTER)
    fill(255, 0, 0)
    rect(x, y, 50, 50)
    
    if keys_pressed[87]:
        y -= 5
        if y <= 25:
            y = 25
    if keys_pressed[83]:
        y += 5
        if y >= 675:
            y = 675
    if keys_pressed[65]:
        x -= 5
        if x <= 25:
            x = 25
    if keys_pressed[68]:
        x += 5
        if x >= 775:
            x = 775

    '''
    for i in range(len(bullet[1])):
        bullet[1][i] += 1
        rect(bullet[0][i], bullet[1][i], 10, 10)
        if bullet[1][i] <= 0:
            del bullet[1][i]
    '''
    bullet[1][0] -= 10
    fill(0, 0, 255)
    ellipse(bullet[0][0], bullet[1][0], 10, 10)
    
def keyPressed():
    global keys_pressed
    keys_pressed[keyCode] = True
    
def keyReleased():
    global keys_pressed
    keys_pressed[keyCode] = False
    
def mousePressed():
    global bullet, x, y
    bullet[0].append(x)
    bullet[1].append(y)  
    del bullet[0][0]
    del bullet[1][0]          
    print(bullet)
    
