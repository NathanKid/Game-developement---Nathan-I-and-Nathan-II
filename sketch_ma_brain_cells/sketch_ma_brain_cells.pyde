bullet = [[0, 0], [0, 0], [0, 0]]#x-coordinate, y-coordinate of player/bullet, lives
enemy = [[400, 100, 3]] #x-coordinate, y-coordinate, lives/17ms hit detection, bullet of enemies
z = True

def setup():
    size(800, 700, P2D)
    frameRate(60)
    smooth()
    cursor(ARROW)
    noLoop() #probably won't work

def draw():
    game()
    framecount()
    
def game():
    global x, y, bullet, enemy, z, enemyBullet, bulletTimerPlayer, healthBar, page, u, bulletTimerEnemy
    background(255)
    stroke(1)
        
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
        
    #enemy desinated movement   
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
