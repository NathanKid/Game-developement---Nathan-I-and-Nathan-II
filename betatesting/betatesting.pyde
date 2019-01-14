keys_pressed = [False for key_code in range(256)]
x, y, playerlives = 400, 550, 3
bullet = [[0, 0]] #x-coordinate, y-coordinate of player/bullet, lives
enemy = [[400, 100, 3]] #x-coordinate, y-coordinate, lives/17ms hit detection, bullet of enemies
enemyBullet = [[400, 100]] #x-coordinate 
z = True
bulletTimer = 0
healthBar = 40
page = 0

button_x = 175
button_y = 350
button_width = 450
button_height = 100
button2_x = 175
button2_y = 500
button2_width = 450
button2_height = 100
button3_x = 175
button3_y = 600
button3_width = 450
button3_height = 60

def setup():
    size(800, 700)
    frameRate(60)
    smooth()
    cursor(ARROW)

def draw():
    global page, button_x, button_y, button_width, button_height, button2_x, button2_y, button2_width, button2_height, button3_x, button3_y, button3_width, button3_height, playerlives 
    rectMode(CORNER)
    noStroke()
    textAlign(LEFT)
    if page == 0:
        titlefont = createFont("Orbitron.ttf", 40)
        buttonfont = createFont("Orbitron.ttf", 60)
        background(0)
        textFont(titlefont)
        textSize(width/9)
        fill(255)
        text("HYPERSPACE", width/18, height/3)
        
        #play button 
        if (mouseX > button_x and mouseX < button_x + button_width and 
                mouseY > button_y and mouseY < button_y + button_height and 
                    mousePressed):
            page = 1
            
        elif (mouseX > button_x and mouseX < button_x + button_width 
                  and mouseY > button_y and mouseY < button_y + button_height):  
            fill(100, 150, 177) 
            
        else:
            fill(5, 70, 177)
            
        rect(button_x, button_y, button_width, button_height, 10)
        textFont(buttonfont)
        fill(255)
        text("PLAY", width/2.6, height/1.65)
        
        #controls/tutorial button
        if (mouseX > button2_x and mouseX < button2_x + button2_width and 
                mouseY > button2_y and mouseY < button2_y + button2_height and 
                    mousePressed):
            page = 2
        elif (mouseX > button2_x and mouseX < button2_x + button2_width and 
                  mouseY > button2_y and mouseY < button2_y + button2_height): 
            fill(100, 150, 177)
        else:
            fill(5, 70, 177)
            
        rect(button2_x, button2_y, button2_width, button2_height, 10)
        textFont(buttonfont)
        fill(255)
        text("CONTROLS", width/3.9,height/1.225)
    
    if page == 1: #Game
        game()
        framecount()
        death()
        
    if page == 2: #Controls
        background(0, 0, 0)
        titlefont2 = createFont("Orbitron.ttf", 40)
        buttonfont2 = createFont("Orbitron.ttf", 50)
        textfont = createFont("Orbitron.ttf", 50)
        descriptionfont = createFont("Orbitron.ttf", 25)
        textFont(titlefont2)
        textSize(width/9)
        text("CONTROLS", width/7, height/6)
        textFont(textfont)
        text("W A S D - Movement", width/16, height/3.5)
        text("LMB - To Fire Cannons", width/16, height/2.5)
        text("RMB - To Fire Rockets", width/16, height/1.9)
        text("L SHIFT - To Open Sheild", width/16, height/1.4)
        textFont(descriptionfont)
        text("Rockets do Splash damage to nearby ships", width/16, height/1.7)        
        text("Shields last 5 seconds and can absorb 5 hits", width/16, height/1.3)
        text("before turning off. Recharging takes 30 seconds", width/16, height/1.22)
        
        if (mouseX > button3_x and mouseX < button3_x + button3_width and 
            mouseY > button3_y and mouseY < button3_y + button3_height and 
            mousePressed):
            page = 0
        elif (mouseX > button3_x and mouseX < button3_x + button3_width and 
                  mouseY > button3_y and mouseY < button3_y + button3_height):  
            fill(100,150,177)
        else:
            fill(5,70,177)
            
        rect(button3_x, button3_y, button3_width, button3_height, 10)
        textFont(buttonfont2)
        fill(255)
        text("BACK TO MENU", width/4.4, height/1.08)
        
    if page == 3: #Player Death
        reset()
        score = 0
        kills = 0
        combo = 0
        background(0,0,0)
        titlefont3 = createFont("Orbitron.ttf", 70)
        buttonfont3 = createFont("Orbitron.ttf", 50)
        statsfont = createFont("Orbitron.ttf", 70)
        noStroke()
        textFont(titlefont3)
        fill(255,0,0)
        text("<< GAME OVER >>", width/11, height/5)
        textFont(statsfont)
        fill(255,0,0)
        text('SCORE: {}'.format(score) , width/16, height/3)
        textFont(statsfont)
        fill(255,0,0)
        text('KILLS: {}'.format(kills) , width/16, height/2.2)
        textFont(statsfont)
        fill(255,0,0)
        text('LIVES LEFT: 0', width/16, height/1.7)
        textFont(statsfont)
        fill(255, 0, 0)
        text('END COMBO: {}'.format(combo) , width/16, height/1.35)
        
        if (mouseX > button3_x and mouseX < button3_x + button3_width and 
            mouseY > button3_y and mouseY < button3_y + button3_height and
            mousePressed):
            page = 0
        elif (mouseX > button3_x and mouseX < button3_x + button3_width and 
            mouseY > button3_y and mouseY < button3_y + button3_height):  
            fill(100, 150, 177)
        else:
            fill(5, 70, 177)
            
        rect(button3_x, button3_y, button3_width, button3_height, 10)
        textFont(buttonfont3)
        fill(255)
        text("BACK TO MENU", width/4.4, height/1.08)
        
    if page == 4: 
        reset()
        score = 0
        kills = 0
        combo = 0
        background(0,0,0)
        titlefont4 = createFont("Orbitron.ttf", 70)
        buttonfont4 = createFont("Orbitron.ttf", 50)
        statsfont2 = createFont("Orbitron.ttf", 70)
        noStroke()
        textFont(titlefont4)
        fill(255, 223, 0)
        text("<< VICTORY >>", width/5.5, height/5)
        textFont(statsfont2)
        fill(255)
        text('SCORE: {}'.format(score) , width/16, height/3)
        textFont(statsfont2)
        text('KILLS: {}'.format(kills) , width/16, height/2.2)
        textFont(statsfont2)
        text('LIVES LEFT: {}'.format(playerlives) , width/16, height/1.7)
        textFont(statsfont2)
        text('END COMBO: {}'.format(combo) , width/16, height/1.35)
        button3_x = 175
        button3_y = 600
        button3_width = 450
        button3_height = 60
        if (mouseX > button3_x and mouseX < button3_x + button3_width and mouseY > button3_y and mouseY < button3_y + button3_height and mousePressed):
            page = 0
        elif (mouseX > button3_x and mouseX < button3_x + button3_width and mouseY > button3_y and mouseY < button3_y + button3_height):  
            fill(100,150,177)
        else:
            fill(5,70,177)
        rect(button3_x, button3_y, button3_width, button3_height, 10)
        textFont(buttonfont4)
        fill(255)
        text("BACK TO MENU", width/4.4,height/1.08)


def game():
    global x, y, bullet, enemy, z, enemyBullet, bulletTimer, healthBar, page
    background(255)
    stroke(1)
    bulletTimer += 1
    
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
    if mousePressed and bulletTimer % 40 == 0:
        del bullet[0][0]
        del bullet[0][0]  
        bullet[0].append(x)
        bullet[0].append(y)   
        
    fill(0, 0, 255)
    ellipse(bullet[0][0], bullet[0][1], 10, 10)
    bullet[0][1] -= 20
    
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
                
            #bullet detection of player
            del bullet[0][0]
            del bullet[0][0]
            bullet[0].append(0)
            bullet[0].append(0) 
        else:
            fill(0, 255, 0)
        
        rect(enemy[0][0], enemy[0][1], 50, 50)
    except:
        pass
  
    try:     
        #enemy desinated movement
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
        
        #bullet
        if bulletTimer >= 75:
            bulletTimer = 0
            
        if bulletTimer % 75 == 0:
            del enemyBullet[0][0]
            del enemyBullet[0][0]
            enemyBullet[0].append(enemy[0][0])
            enemyBullet[0].append(enemy[0][1])
            
        fill(128, 0, 128)
        ellipse(enemyBullet[0][0], enemyBullet[0][1], 10, 10)
        enemyBullet[0][1] += 10
    
    #health bar of enemy
        if 40 / 3 * u / 40 * 100 <= 66.6666666666666:
            healthBar = 40 / 3 * u
        elif 40 / 3 * 1 / 40 * 100 <= 33.33333333333333:
            healthBar = 40 / 3 * u
        
        fill(0, 255, 0)    
        rectMode(CORNER)
        rect(enemy[0][0] - 22.5, enemy[0][1] - 35, healthBar, 5)
        
    except:
        pass
        
def death():
    global x, y, enemy, playerlives, page
    try:
        if (enemy[0][0] >= x - 25 and enemy[0][0] <= x + 25 and 
            enemy[0][1] >= y - 25 and enemy[0][1] <= y + 25):
            playerlives = 0
            page = 3
        if (x - 25 <= enemyBullet[0][0] - 10 and x + 25 >= enemyBullet[0][0] + 10 and 
            y - 25 <= enemyBullet[0][1] - 10 and y + 25 >= enemyBullet[0][1] + 10):
            playerlives -= 1
    except:
       pass  
    
    if playerlives == 0:
            page = 3

def reset():
    global x, y, playerlives, bullet, enemy, enemyBullet, z, bulletTimer, healthBar, page
    x, y, playerlives = 400, 550, 3
    bullet = [[0, 0]] #x-coordinate, y-coordinate of player/bullet, lives
    enemy = [[400, 100, 3]] #x-coordinate, y-coordinate, lives/17ms hit detection, bullet of enemies
    enemyBullet = [[400, 100]] #x-coordinate 
    z = True
    bulletTimer = 0
    healthBar = 40

def framecount():
    global enemy
    rectMode(CORNER)
    fill(0, 0, 0, 150)
    rect(0, 0, 45, 15)
    a = int(frameRate // 1)
    textSize(12)
    textAlign(LEFT, TOP)
    
    if a <= 30:
        fill(255, 0, 0)
    else:
        fill(0, 255, 0)
        
    text('fps:{}'.format(a), 0, 0)
    
def keyPressed():
    global keys_pressed
    keys_pressed[keyCode] = True
    
def keyReleased():
    global keys_pressed
    keys_pressed[keyCode] = False

def mousePressed():
    global bullet, x, y
    del bullet[0][0]
    del bullet[0][0]   
    bullet[0].append(x)
    bullet[0].append(y)  
