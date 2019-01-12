keys_pressed = [False for key_code in range(256)]
x, y, lives = 400, 550, 3
bullet = [[0],[0],[0]] #x-coordinate, y-coordinate of player/bullet, lives
enemy = [[400, 100, 100]] #x-coordinaddte, y-coordinate, lives/17ms hit detection, bullet of enemies
z = True

def setup():
    size(800, 700, P2D)
    frameRate(60)

def draw():
    game()
    framecount()
    suicide()
    
def game():
    global x, y, bullet, enemy, z
    background(255)
    
    rectMode(CENTER)
    fill(255, 0, 0)
    rect(x, y, 50, 50)
    
    if keys_pressed[87]:
        y -= 6
        if y <= 25:
            y = 25
    if keys_pressed[83]:
        y += 6
        if y >= 675:
            y = 675
    if keys_pressed[65]:
        x -= 6
        if x <= 25:
            x = 25
    if keys_pressed[68]:
        x += 6
        if x >= 775:
            x = 775
    
    bullet[1][0] -= 20
    fill(0, 0, 255)
    rect(bullet[0][0], bullet[1][0], 10, 10)

    #enemy death

    try:
        if (enemy[0][0] - 25 <= bullet[0][0] <= enemy[0][0] + 25 and 
                bullet[1][0] >= enemy[0][1] - 25 and 
                    bullet[1][0] <= enemy[0][1] + 25):
            fill(255, 0, 0)
            u = enemy[0][2] - 1
            del enemy[0][2]
            enemy[0].append(u)
            if enemy[0][2] == 0:
                del enemy[0]
            print(enemy)
        else:
            fill(0, 255, 0)
        
        rect(enemy[0][0], enemy[0][1], 50, 50)
        
        if z:
            enemy[0][0] += 2
            enemy[0][1] += 0.5
            if enemy[0][0] > 750:
                z = False
        if not z:
            enemy[0][0] -= 2
            enemy[0][1] += 0.5
            if enemy[0][0] < 50:
                z = True
        if enemy[0][1] >= 700:
            enemy[0][1] = -25
            z = True
    except:
        pass
        
def suicide():
    global x, y, enemy
    if (enemy[0][0] >= x - 25 and enemy[0][0] <= x + 25 and 
            enemy[0][1] >= y - 25 and enemy[0][1] <= y + 25):
        lives = 0
        print(lives)
        exit() 
            
def framecount():
    a = int(frameRate // 1)
    textAlign(LEFT, TOP)
    fill(0)
    text('fps:{}'.format(a), 0, 0)
    
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
