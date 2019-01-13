page = 0

def setup():
    titlefont = createFont("Orbitron.ttf", 40)
    buttonfont = createFont("Orbitron.ttf", 60)
    size(800,700)

def draw():
    global page
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
    if page == 0:
        titlefont = createFont("Orbitron.ttf", 40)
        buttonfont = createFont("Orbitron.ttf", 60)
        background(0)
        textFont(titlefont)
        textSize(width/9)
        fill(255)
        text("HYPERSPACE",width/18,height/3)
        #play button 
        noStroke()
        if (mouseX > button_x and mouseX < button_x + button_width and
                mouseY > button_y and mouseY < button_y + button_height and mousePressed):
            page = 1
            
        elif (mouseX > button_x and mouseX < button_x + button_width and
                mouseY > button_y and mouseY < button_y + button_height):  
            fill(100,150,177) 
            
        else:
            fill(5,70,177)
        rect(button_x, button_y, button_width, button_height, 10)
        
        textFont(buttonfont)
        fill(255)
        text("PLAY", width/2.6,height/1.65)
        
        #controls/tutorial button
        noStroke()
        if (mouseX > button2_x and mouseX < button2_x + button2_width and
                mouseY > button2_y and mouseY < button2_y + button2_height and mousePressed):
            page = 2
        elif (mouseX > button2_x and mouseX < button2_x + button2_width and
                mouseY > button2_y and mouseY < button2_y + button2_height): 
            fill(100,150,177)
        else:
            fill(5,70,177)
        rect(button2_x, button2_y, button2_width, button2_height, 10)
        
        textFont(buttonfont)
        fill(255)
        text("CONTROLS", width/3.9,height/1.225)
    
    if page == 1: #Game
        background(255,0,0)
        
    if page == 2: #Controls
        background(0,0,0)
        titlefont = createFont("Orbitron.ttf", 40)
        buttonfont = createFont("Orbitron.ttf", 50)
        textfont = createFont("Orbitron.ttf", 50)
        descriptionfont = createFont("Orbitron.ttf", 25)
        textFont(titlefont)
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
        if (mouseX > button3_x and mouseX < button3_x + button3_width and mouseY > button3_y and mouseY < button3_y + button3_height and mousePressed):
            page = 0
        elif (mouseX > button3_x and mouseX < button3_x + button3_width and mouseY > button3_y and mouseY < button3_y + button3_height):  
            fill(100,150,177)
        else:
            fill(5,70,177)
        rect(button3_x, button3_y, button3_width, button3_height, 10)
        textFont(buttonfont)
        fill(255)
        text("BACK TO MENU", width/4.4,height/1.08)
        
    if page == 3: #Player Death
        score = 0
        kills = 0
        playerlives = 3
        combo = 0
        background(0,0,0)
        titlefont = createFont("Orbitron.ttf", 70)
        buttonfont = createFont("Orbitron.ttf", 50)
        statsfont = createFont("Orbitron.ttf", 70)
        noStroke()
        textFont(titlefont)
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
        text('LIVES LEFT: {}'.format(playerlives) , width/16, height/1.7)
        textFont(statsfont)
        fill(255,0,0)
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
        textFont(buttonfont)
        fill(255)
        text("BACK TO MENU", width/4.4,height/1.08)
        
        
        
def mousePressed():
    print(mouseX, mouseY)
