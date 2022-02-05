# pygame atari ver 10.2  By : M.H.Khademi
# Date: 99-12-1
import pygame                      # import pygame library
import time                        # import  time  library
import random                      # import random library
pygame.init()                      # set defalt pygame setting
plane_width = 48
display_width = 800
display_height = 600
crash_sound = pygame.mixer.Sound("sounds\\lose.wav")
pygame.mixer.music.load("sounds\\main.ogg")
direct = 0                         #  set direct to 0
white  = (255,255,255)             #  set white   color
Blue   = (0,0,255)                 #  set blue    color
dBlue   = (20,20,150)              #  set Dark Blue    color
yellow = (255,255,100)             #  set yellow  color
dyellow = (255,255,200)             #  set yellow  color
black  = (0,0,0)                   #  set  black  color
green  = (0,255,0)                 #  set  green  color
dGreen = (0,120,0)                 #  set Dark Green color
red    = (255,0,0)                 #  set   red   color
dRed   = (120,0,0)                 #  set  Dark Red  color
grey   = (230,230,230)             #  set  gray   color
color = [(255,255,255),(255,255,100),(255,0,0),(0,255,0),(0,0,255),(255,0,255),(0,255,255),(255,255,0)]                     #  set color list
gameDisplay = pygame.display.set_mode((display_width,display_height))              #  set gameDisplay window
clock = pygame.time.Clock()
gameDisplay.fill(white)            #  set gameDisplay fill color
pygame.display.set_caption("M.H.KH - atary")           #  set gameDisplay caption
icon = pygame.image.load("icon\\a.png")                #  load gameDisplay icon
bg = pygame.image.load("images\\b.jpg")                #  load gameDisplay background
Bg = pygame.transform.scale( bg , (800 , 600))         #  scale the bg
pygame.display.set_icon(icon)                          #  set gameDisplay icon
gameDisplay.blit( Bg , (0,0))                          #  set gameDisplay background
planeimgNormal = pygame.image.load("images\\planeimg.png")      #  load abject image
planeimgLeft   = pygame.image.load("images\\planeLeft.png")     #  load abject image
planeimgRight  = pygame.image.load("images\\planeRight.png")    #  load abject image

#********** def button ()  ****************

def button (msg , x , y , w , h , ic , ac , br , btlr , btrr , bblr , action = None):

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x < mouse[0] < x+w and y < mouse[1] < y+h:
        pygame.draw.rect(gameDisplay , ac , (x,y,w,h) , border_radius=br , border_top_left_radius=btlr , border_top_right_radius=btrr , border_bottom_left_radius=bblr)
        if click[0] == True and action != None:
            if action == "play":
                game_loop()
            elif action == "quit":
                pygame.quit()
                quit()
    else :
        pygame.draw.rect(gameDisplay , ic , (x,y,w,h) , border_radius=15 , border_top_left_radius=15 , border_top_right_radius=15 , border_bottom_left_radius=15)
    smallText = pygame.font.Font('fonts\\freesansbold.ttf',20)
    TextSurf  = smallText.render(msg,True,white)
    TextRect  = TextSurf.get_rect()
    TextRect.center = ((x+w/2),(y+h/2))
    gameDisplay.blit(TextSurf,TextRect)

#********** def game_intro ()  ****************
def game_intro ():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        largeText = pygame.font.Font('fonts\\freesansbold.ttf',75)
        TextSurf  = largeText.render(" Atari Game ",True,black)
        TextRect  = TextSurf.get_rect()
        TextRect.center = ((display_width/2),(display_height/5))
        gameDisplay.blit(TextSurf,TextRect)
        button("Play!" , 250 , 350 , 300 , 70 , dGreen , green , 15 , 15 , 15 , 15 , "play")
        button("Quit " , 250 , 450 , 300 , 70 , dRed , red , 15 , 15 , 15 , 15 , "quit") 
        pygame.display.update()

#********** def Try_Again ()  ****************
def Try_Again (passed):
    f = open('score.txt', 'r+')
    f.writelines(str(passed))
    f.close()
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        largeText = pygame.font.Font('fonts\\freesansbold.ttf',75)
        TextSurf  = largeText.render(" You Crashed ",True,black)
        TextRect  = TextSurf.get_rect()
        TextRect.center = ((display_width/2),(display_height/3))
        gameDisplay.blit(TextSurf,TextRect)
        button("Try Again!" , 250 , 350 , 300 , 70 , dGreen , green , 15 , 15 , 15 , 15 , "play")
        button("Quit " , 250 , 450 , 300 , 70 , dRed , red , 15 , 15 , 15 , 15 , "quit") 
        pygame.display.update()

#********** def stuffe_score ()  ****************
def print_score (passed):
    font = pygame.font.SysFont(None,25)
    text = font.render("Score: "+str(passed),True ,yellow)
    gameDisplay.blit(text,(0,0))

#********** def message_display ()  ****************

def message_display (text , size , color):
    largeText = pygame.font.Font('fonts\\Roboto-Black.ttf', size)
    TextSurf  = largeText.render(text , True , color)
    TextRect  = TextSurf.get_rect()
    TextRect.center = ((display_width/2) , (display_height/3))
    gameDisplay.blit(TextSurf , TextRect)
    pygame.display.update()

#********** def stuff ()  ****************

def stuff (stuff_x , stuff_y ,stuff_w ,stuff_h ,stuff_color):
    pygame.draw.rect(gameDisplay ,stuff_color ,[stuff_x , stuff_y ,stuff_w ,stuff_h])

#********** def plane ()  ****************
    
def plane (x,y):
    global direct
    if direct == 0:
        gameDisplay.blit(planeimgNormal , ( x , y))
    if direct == -1:
        gameDisplay.blit(planeimgLeft , ( x , y))
    if direct == +1:
        gameDisplay.blit(planeimgRight , ( x , y))
    
#********** def crash ()  ****************
    
def crash ():
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(crash_sound)
    message_display( "You Crashed" , 100 , yellow)
                     
#********** def game_loop ()  ****************
                     
def game_loop ():
    crashed = False
    # f = open('score.txt')
    # passed = int(f.read())
    passed = 0
    pygame.mixer.music.play(-1)
    x = display_width * 0.48
    y = display_height * 0.9
    delta_x = 0
    delta_y = 0
    stuff_start_x = random.randrange(0 , display_width)
    stuff_start_y = -700
    stuff_width = 100
    stuff_height = 100
    stuff_speed = 3
    while not crashed:
        global direct
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                crashed = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    delta_x = -3
                    direct = -1
                elif event.key == pygame.K_RIGHT:
                    delta_x = 3
                    direct = +1
                if event.key == pygame.K_UP:
                    delta_y = -3
                elif event.key == pygame.K_DOWN:
                    delta_y = 3
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    delta_x = 0
                    direct = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    delta_y = 0
        random.shuffle(color)
        color_number = random.randrange(0 , 7)
        gameDisplay.blit( Bg , (0,0))
        x += delta_x
        y += delta_y
        if y > display_height -100:
            y = display_height -100
        if y < 100:
            y=100
        print_score(passed)
        stuff_color = color[color_number]
        stuff(stuff_start_x , stuff_start_y ,stuff_width ,stuff_height ,stuff_color)
        stuff_start_y += stuff_speed
        plane(x , y)
        if y < stuff_start_y + stuff_height and y + plane_width > stuff_start_y :
            if x > stuff_start_x and x < stuff_start_x + stuff_width or \
                x + plane_width > stuff_start_x and x + plane_width < stuff_start_x + stuff_width :
                crash()
                time.sleep(5)
                Try_Again(passed)
        if x > display_width - plane_width or x < 0 :
            crash()
            time.sleep(5)
            Try_Again()
        if stuff_start_y > display_height :
            stuff_color = color[color_number]
            stuff_start_y = -stuff_height
            stuff_start_x = random.randrange(0 , display_width)
            passed += 1
            if passed % 4 == 0:
                stuff_speed += 1
        pygame.display.update()
        clock.tick(120)
        
#********** end def game_loop ()  ****************

game_intro()     
game_loop()     
pygame.quit()
quit()
