keys_pressed = [False for key_code in range(256)]
x, y, playerlives = 400, 550, 3
bullet = [[0, 0], [0, 0], [0, 0]]#x-coordinate, y-coordinate of player/bullet, lives
enemy = [[400, 100, 3]] #x-coordinate, y-coordinate, lives/17ms hit detection, bullet of enemies
enemyBullet = [[400, 100]] #x-coordinate 
z = True
bulletTimerPlayer = 0
bulletTimerEnemy = 0
healthBar = 40
page = 0
u = enemy[0][2]

def setup():
    size(800, 700, P2D)
    frameRate(60)
    smooth()
    cursor(ARROW)
    noLoop() #probably won't work

def draw():
    game()
    framecount()
    death()
    
def game():
    global x, y, bullet, enemy, z, enemyBullet, bulletTimerPlayer, healthBar, page, u, bulletTimerEnemy
    background(255)
    stroke(1)
    
    #main player
    rectMode(CENTER)
    fill(255, 0, 0)
    rect(x, y, 50, 50)
    
    #movement
    if keys_pressed[87]: #forward
        y -= 6
        if y <= 25:
            y = 25
    if keys_pressed[83]: #back
        y += 6
        if y >= 675:
            y = 675
    if keys_pressed[65]: #left
        x -= 6
        if x <= 25:
            x = 25
    if keys_pressed[68]: #right
        x += 6
        if x >= 775:
            x = 775
            
    #bullets
    if mousePressed:
        bulletTimerPlayer += 1 
        
    if bulletTimerPlayer == 1:
        del bullet[0][0]
        del bullet[0][0]  
        bullet[0].append(x)
        bullet[0].append(y) 
            
    if bulletTimerPlayer == 21:
        del bullet[1][0]
        del bullet[1][0]
        bullet[1].append(x)
        bullet[1].append(y)

    if bulletTimerPlayer == 41: 
        del bullet[2][0]
        del bullet[2][0]
        bullet[2].append(x)
        bullet[2].append(y)
        
    if bulletTimerPlayer >= 71:
        bulletTimerPlayer = 0

    fill(0, 0, 255)
    bullet[0][1] -= 20
    bullet[1][1] -= 20
    bullet[2][1] -= 20
    rect(bullet[0][0], bullet[0][1], 10, 10)
    rect(bullet[1][0], bullet[1][1], 10, 10)
    rect(bullet[2][0], bullet[2][1], 10, 10)
        
    #enemy death
    try:
        #enemy hit
        if (enemy[0][0] - 25 <= bullet[0][0] <= enemy[0][0] + 25 and 
            bullet[0][1] >= enemy[0][1] - 25 and 
            bullet[0][1] <= enemy[0][1] + 25):
            fill(255, 0, 0)
            u = enemy[0][2] - 1
            del enemy[0][2]
            enemy[0].append(u)
            if enemy[0][2] == 0:
                del enemy[0]
                page = 4
            del bullet[0][0]
            del bullet[0][0]
            bullet[0].append(0)
            bullet[0].append(0) 
            
        elif (enemy[0][0] - 25 <= bullet[1][0] <= enemy[0][0] + 25 and
            bullet[1][1] >= enemy[0][1] - 25 and 
            bullet[1][1] <= enemy[0][1] + 25):
            fill(255, 0, 0)
            u = enemy[0][2] - 1
            del enemy[0][2]
            enemy[0].append(u)
            if enemy[0][2] == 0:
                del enemy[0]
                page = 4
            del bullet[1][0]
            del bullet[1][0]
            bullet[1].append(0)
            bullet[1].append(0)
            
        elif (enemy[0][0] - 25 <= bullet[2][0] <= enemy[0][0] + 25 and 
            bullet[2][1] >= enemy[0][1] - 25 and 
            bullet[2][1] <= enemy[0][1] + 25):
            fill(255, 0, 0)
            u = enemy[0][2] - 1
            del enemy[0][2]
            enemy[0].append(u)
            if enemy[0][2] == 0:
                del enemy[0]
                page = 4
            del bullet[2][0]
            del bullet[2][0]
            bullet[2].append(0)
            bullet[2].append(0)
        else:
            fill(0, 255, 0)
        
        rect(enemy[0][0], enemy[0][1], 50, 50)
        
        #health bar of enemy
        if 40 / 3 * u / 40 * 100 <= 66:
            healthBar = 40 / 3 * u
        elif 40 / 3 * 1 / 40 * 100 <= 33:
            healthBar = 40 / 3 * u
            
        fill(0, 255, 0)   
        rectMode(CORNER)
        rect(enemy[0][0] - 21, enemy[0][1] - 35, healthBar, 5)
    except:
        pass
    
    #enemy desinated movement
    try:     
        if z:
            enemy[0][0] += 4
            enemy[0][1] += 1
            if enemy[0][0] > 750:
                z = False    
        if not z:
            enemy[0][0] -= 3
            enemy[0][1] += 2
            if enemy[0][0] < 50:
                z = True
                
        if enemy[0][1] >= 700:
            enemy[0][1] = - 25
            z = True
        
        #bullet
        bulletTimerEnemy += 1
        if bulletTimerEnemy % 75 == 0:
            del enemyBullet[0][0]
            del enemyBullet[0][0]
            enemyBullet[0].append(enemy[0][0])
            enemyBullet[0].append(enemy[0][1])
            
        fill(128, 0, 128)
        rectMode(CENTER)
        rect(enemyBullet[0][0], enemyBullet[0][1], 10, 10)
        enemyBullet[0][1] += 10
        
        if bulletTimerEnemy >= 75:
            bulletTimerEnemy = 0
    except:
        pass
            
def death():
    global x, y, enemy, playerlives, page
    try:
        if (enemy[0][0] >= x - 45 and enemy[0][0] <= x + 45 and 
            enemy[0][1] >= y - 45 and enemy[0][1] <= y + 45):
            playerlives = 0
            page = 3
            exit()
            
        if (x - 35 <= enemyBullet[0][0] - 10 and x + 35 >= enemyBullet[0][0] + 10 and 
            y - 35 <= enemyBullet[0][1] - 10 and y + 35 >= enemyBullet[0][1] + 10):
            playerlives -= 1
            exit()
    except:
       pass 
    
    if playerlives == 0:
            page = 3

def reset():
    global x, y, playerlives, bullet, enemy, enemyBullet, z, bulletTimer, healthBar, page
    x, y, playerlives = 400, 550, 3
    bullet = [[0, 0], [0, 0], [0, 0]] #x-coordinate, y-coordinate of player/bullet, lives
    enemy = [[400, 100, 3]] #x-coordinate, y-coordinate, lives/17ms hit detection, bullet of enemies
    enemyBullet = [[400, 100]] #x-coordinate 
    z = True
    bulletTimer = 0
    healthBar = 40

def framecount():
    global enemy
    noStroke()
    rectMode(CORNER)
    fill(0, 0, 0, 150)
    rect(0, 0, 42, 15)
    a = int(frameRate // 1)
    textSize(12)
    textAlign(LEFT, TOP)
    
    if a <= 30:
        fill(255, 0, 0)
    else:
        fill(0, 255, 0)
        
    text('fps:{}'.format(a), 2, 0)
    
def keyPressed():
    global keys_pressed
    keys_pressed[keyCode] = True
    
def keyReleased():
    global keys_pressed
    keys_pressed[keyCode] = False
    
def mousePressed(): #probably won't work
    loop() 

def mouseReleased():
    global bulletTimerPlayer
    bulletTimerPlayer = 0
