keys_pressed = [False for key_code in range(256)]
x, y, playerlives = 400, 550, 3
bullet = []#x-coordinate, y-coordinate of player/bullet, lives
enemy = [[400, 100, 3], [300, 100, 3], [500, 100, 3]] #x-coordinate, y-coordinate, lives/17ms hit detection, bullet of enemies
enemyBullet = [[400, 100], [300, 100], [500, 100]] #x-coordinate 
z = True
bulletTimerPlayer = 0
bulletTimerEnemy = 0
healthBar = 40
page = 0
u = enemy[0][2]
d = enemy[1][2]
e = enemy[2][2]
clickTimer = True
a = 0
c = 0

def setup():
    size(800, 700)
    frameRate(60)
    smooth()
    cursor(ARROW)
    noLoop()

def draw():
    game()
    framecount()
    
def game():
    global newlist, x, y, bullet, enemy, z, enemyBullet, bulletTimerPlayer, healthBar, page, u, bulletTimerEnemy, clickTimer, a, d, e, c, i 
    background(255)
    stroke(1)
    
    #main player
    rectMode(CENTER)
    fill(255, 0, 0, 0)
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
        
    if not clickTimer:
        a += 1 
        if a >= 25:
            clickTimer = True        
    #bullets
    
    try:
        if mousePressed and clickTimer:
            fill(0, 0, 255)
            bullet.append([x, y])
            
        for i in range(len(bullet)):
            rect(bullet[i][0], bullet[i][1], 10, 10)
            bullet[i][1] -= random(0, 20)
        print(bullet)
            
    except:
        pass

    #enemy death
    '''
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
            del bullet[2][0]
            del bullet[2][0]
            bullet[2].append(0)
            bullet[2].append(0)
        else:
            fill(0, 255, 0)
            
        rect(enemy[0][0], enemy[0][1], 50, 50)
    except:
        pass
    
    try:    #next
        if (enemy[1][0] - 25 <= bullet[0][0] <= enemy[1][0] + 25 and 
            bullet[0][1] >= enemy[1][1] - 25 and 
            bullet[0][1] <= enemy[1][1] + 25):
            fill(255, 0, 0)
            d = enemy[1][2] - 1
            del enemy[1][2]
            enemy[1].append(d)
            if enemy[1][2] == 0:
                del enemy[1]
            del bullet[0][0]
            del bullet[0][0]
            bullet[0].append(0)
            bullet[0].append(0) 
            
        elif (enemy[1][0] - 25 <= bullet[1][0] <= enemy[1][0] + 25 and
            bullet[1][1] >= enemy[1][1] - 25 and 
            bullet[1][1] <= enemy[1][1] + 25):
            fill(255, 0, 0)
            d = enemy[1][2] - 1
            del enemy[1][2]
            enemy[0].append(d)
            if enemy[1][2] == 0:
                del enemy[1]
            del bullet[1][0]
            del bullet[1][0]
            bullet[1].append(0)
            bullet[1].append(0)
            
        elif (enemy[1][0] - 25 <= bullet[2][0] <= enemy[1][0] + 25 and 
            bullet[2][1] >= enemy[1][1] - 25 and 
            bullet[2][1] <= enemy[1][1] + 25):
            fill(255, 0, 0)
            d = enemy[1][2] - 1
            del enemy[1][2]
            enemy[1].append(d)
            if enemy[1][2] == 0:
                del enemy[0]
            del bullet[2][0]
            del bullet[2][0]
            bullet[2].append(0)
            bullet[2].append(0)
        else:
            fill(0, 255, 0)
        
        rect(enemy[1][0], enemy[1][1], 50, 50)
    except:
        pass

    try: #after
        #enemy hit
        if (enemy[2][0] - 25 <= bullet[0][0] <= enemy[2][0] + 25 and 
            bullet[0][1] >= enemy[2][1] - 25 and 
            bullet[0][1] <= enemy[2][1] + 25):
            fill(255, 0, 0)
            e = enemy[2][2] - 1
            del enemy[2][2]
            enemy[2].append(e)
            if enemy[2][2] == 0:
                del enemy[2]
            del bullet[0][0]
            del bullet[0][0]
            bullet[0].append(0)
            bullet[0].append(0) 
            
        elif (enemy[2][0] - 25 <= bullet[1][0] <= enemy[2][0] + 25 and
            bullet[1][1] >= enemy[2][1] - 25 and 
            bullet[1][1] <= enemy[2][1] + 25):
            fill(255, 0, 0)
            e = enemy[2][2] - 1
            del enemy[2][2]
            enemy[2].append(e)
            if enemy[2][2] == 0:
                del enemy[2]
            del bullet[1][0]
            del bullet[1][0]
            bullet[1].append(0)
            bullet[1].append(0)
            
        elif (enemy[2][0] - 25 <= bullet[2][0] <= enemy[2][0] + 25 and 
            bullet[2][1] >= enemy[2][1] - 25 and 
            bullet[2][1] <= enemy[2][1] + 25):
            fill(255, 0, 0)
            e = enemy[2][2] - 1
            del enemy[2][2]
            enemy[2].append(e)
            if enemy[2][2] == 0:
                del enemy[2]
            del bullet[2][0]
            del bullet[2][0]
            bullet[2].append(0)
            bullet[2].append(0)
        else:
            fill(0, 255, 0)
            
        rect(enemy[2][0], enemy[2][1], 50, 50)
    except:
        pass
        
    try:
        if 40 / 3 * u / 40 * 100 <= 66:
            healthBar = 40 / 3 * u
        elif 40 / 3 * 1 / 40 * 100 <= 33:
            healthBar = 40 / 3 * u
            fill(255, 0, 0)

        fill(0, 255, 0)
        rectMode(CORNER)
        rect(enemy[0][0] - 21, enemy[0][1] - 35, healthBar, 5)
        
        if 40 / 3 * d / 40 * 100 <= 66:
            healthBar = 40 / 3 * d
        elif 40 / 3 * 1 / 40 * 100 <= 33:
            healthBar = 40 / 3 * d
            
        fill(0, 255, 0)   
        rectMode(CORNER)
        rect(enemy[1][0] - 21, enemy[1][1] - 35, healthBar, 5)
        
        if 40 / 3 * e / 40 * 100 <= 66:
            healthBar = 40 / 3 * e
        elif 40 / 3 * 1 / 40 * 100 <= 33:
            healthBar = 40 / 3 * e
            
        fill(0, 255, 0)   
        rectMode(CORNER)
        rect(enemy[2][0] - 21, enemy[2][1] - 35, healthBar, 5)
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
    except:
        pass
        
    try: #next
        if z:
            enemy[1][0] += 4
            enemy[1][1] += 1
            if enemy[0][0] > 750:
                z = False    
        if not z:
            enemy[1][0] -= 3
            enemy[1][1] += 2
            if enemy[0][0] < 50:
                z = True
                
        if enemy[1][1] >= 700:
            enemy[1][1] = - 25
            z = True
    except:
        pass
        
    try: #after  
        if z:
            enemy[2][0] += 4
            enemy[2][1] += 1
            if enemy[0][0] > 750:
                z = False    
        if not z:
            enemy[2][0] -= 3
            enemy[2][1] += 2
            if enemy[0][0] < 50:
                z = True
                
        if enemy[2][1] >= 700:
            enemy[2][1] = - 25
            z = True
    except:
        pass
    
    try:
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
    except:
        pass
        
    try:
        if bulletTimerEnemy % 95 == 0:
            del enemyBullet[1][0]
            del enemyBullet[1][0]
            enemyBullet[1].append(enemy[1][0])
            enemyBullet[1].append(enemy[1][1])
            
        fill(128, 0, 128)
        rectMode(CENTER)
        rect(enemyBullet[1][0], enemyBullet[1][1], 10, 10)
        enemyBullet[1][1] += 10
        
    except:
        pass
    
    try:
        if bulletTimerEnemy % 85 == 0:
            del enemyBullet[2][0]
            del enemyBullet[2][0]
            enemyBullet[2].append(enemy[2][0])
            enemyBullet[2].append(enemy[2][1])
            
        fill(128, 0, 128)
        rectMode(CENTER)
        rect(enemyBullet[2][0], enemyBullet[2][1], 10, 10)
        enemyBullet[2][1] += 10
        
    except:
        pass
        
        if bulletTimerEnemy >= 90:
            bulletTimerEnemy = 0
    
    print(enemy)
            
def death():
    global x, y, enemy, playerlives, page
    try:
        if (enemy[0][0] >= x - 45 and enemy[0][0] <= x + 45 and 
            enemy[0][1] >= y - 45 and enemy[0][1] <= y + 45):
            exit()
        
        if (enemy[1][0] >= x - 45 and enemy[1][0] <= x + 45 and 
            enemy[1][1] >= y - 45 and enemy[1][1] <= y + 45):
            exit()
            
        if (enemy[2][0] >= x - 45 and enemy[2][0] <= x + 45 and 
            enemy[2][1] >= y - 45 and enemy[2][1] <= y + 45):
            exit()
            
        if (x - 35 <= enemyBullet[0][0] - 10 and x + 35 >= enemyBullet[0][0] + 10 and 
            y - 35 <= enemyBullet[0][1] - 10 and y + 35 >= enemyBullet[0][1] + 10):
            exit()
            
        if (x - 35 <= enemyBullet[1][0] - 10 and x + 35 >= enemyBullet[1][0] + 10 and 
            y - 35 <= enemyBullet[1][1] - 10 and y + 35 >= enemyBullet[1][1] + 10):
            exit()
            
        if (x - 35 <= enemyBullet[2][0] - 10 and x + 35 >= enemyBullet[2][0] + 10 and 
            y - 35 <= enemyBullet[2][1] - 10 and y + 35 >= enemyBullet[2][1] + 10):
            exit()
    except:
       pass 
    '''

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
    
def mousePressed():
    loop()
    
def mouseReleased():
    global bulletTimerPlayer, clickTimer, a, bullet
    bulletTimerPlayer = 0
    clickTimer = False
    a = 0
    
    for h in range(len(bullet)):
        if bullet[len(bullet) - 1][1] < 0:
            del bullet[0]

    
