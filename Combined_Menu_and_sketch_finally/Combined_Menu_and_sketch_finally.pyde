y = 560 #y-axis of bullet
page = 0
BTN_HOVER = "#F3DFA2"
right_Pressed = False
left_Pressed = False


def setup():
    size(800,700)
    frameRate(60)
    noStroke()

def draw():
    global page
    
    if page == 0:
        background(0)
        titlefont = createFont("Orbitron.ttf", 40)
        buttonfont = createFont("Orbitron.ttf", 60)
        textFont(titlefont)
        textSize(width/9)
        fill(255)
        text("HYPERSPACE",width/18,height/3)
        
        #play button 
        button_x = 175
        button_y = 350
        button_width = 450
        button_height = 100
        
        if (mouseX > button_x and mouseX < button_x + button_width and
                mouseY > button_y and mouseY < button_y + button_height and mousePressed):
            page = 1

        elif (mouseX > button_x and mouseX < button_x + button_width and
                mouseY > button_y and mouseY < button_y + button_height):  # Hovering
            fill(100,150,177) 
            
        else:
            fill(5,70,177)
        rect(button_x, button_y, button_width, button_height, 10)
        
        textFont(buttonfont)
        fill(255)
        text("PLAY", width/2.6,height/1.65)
        
        #controls/tutorial button
        button2_x = 175
        button2_y = 500
        button2_width = 450
        button2_height = 100
        
        if (mouseX > button2_x and mouseX < button2_x + button2_width and
                mouseY > button2_y and mouseY < button2_y + button2_height and mousePressed):
            page = 2
        elif (mouseX > button2_x and mouseX < button2_x + button2_width and
                mouseY > button2_y and mouseY < button2_y + button2_height):  # Hovering
            fill(100,150,177)
        else:
            fill(5,70,177)
        rect(button2_x, button2_y, button2_width, button2_height, 10)
        
        textFont(buttonfont)
        fill(255)
        text("CONTROLS", width/3.9,height/1.225)
    
    if page == 1:
        game()
    if page == 2:
        background(255, 255, 0)
        
def game():
    global y, x, right_Pressed, left_Pressed
    background(0, 255, 0)
    rectMode(CENTER)
    rect(400, 580, 50, 50)
    
    #bullet
    fill(255, 0, 0)
    rect(400, y, 10, 10)
    
    if mousePressed and left_Pressed:
        y = y - 10
        if y <= 0:
            y = 560
    elif not mousePressed:
        if y > - 1:
            y = y - 10
    
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

    

    
