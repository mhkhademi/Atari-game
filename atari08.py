# pygame atari ver 8.0  By : M.H.Khademi
# Date: 99-11-20
import pygame
import time
import random
pygame.init()
plane_width = 48
display_width = 800
display_height = 600
crashed_sound = pygame.mixer.Sound("sounds\\lose.wav")
pygame.mixer.music.load("sounds\\main.ogg")
white = (255,255,255)
yellow = (255,255,100)
color = [(255,255,255),(255,255,100),(255,0,0),(0,255,0),(0,0,255),(255,0,255),(0,255,255),(255,255,0)]
gameDisplay = pygame.display.set_mode((display_width,display_height))
clock = pygame.time.Clock()
gameDisplay.fill(white)
pygame.display.set_caption("M.H.KH - atary")
icon = pygame.image.load("icon\\a.png")
bg = pygame.image.load("images\\b.jpg")
Bg = pygame.transform.scale( bg , (800 , 600))
pygame.display.set_icon(icon)
gameDisplay.blit( Bg , (0,0))
planeimg = pygame.image.load("images\\planeimg.png")

#********** def stuffe_score ()  ****************
def print_score(passed):
    font = pygame.font.SysFont(None,25)
    text = font.render("Score: "+str(passed),True ,yellow)
    gameDisplay.blit(text,(0,0))

#********** def message_display ()  ****************

def message_display(text , size , color):
    largeText = pygame.font.Font('fonts\\Roboto-Black.ttf', size)
    TextSurf  = largeText.render(text , True , color)
    TextRect  = TextSurf.get_rect()
    TextRect.center = ((display_width/2) , (display_height/3))
    gameDisplay.blit(TextSurf , TextRect)
    pygame.display.update()
    time.sleep( 7 )
    game_loop ()

#********** def stuff ()  ****************

def stuff(stuff_x , stuff_y ,stuff_w ,stuff_h ,stuff_color):
    pygame.draw.rect(gameDisplay ,stuff_color ,[stuff_x , stuff_y ,stuff_w ,stuff_h])

#********** def plane ()  ****************
    
def plane(x,y):
    gameDisplay.blit(planeimg , ( x , y))
    
#********** def crash ()  ****************
    
def crash():
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(crashed_sound)
    message_display( "You Crashed" , 100 , yellow)
                     
#********** def game_loop ()  ****************
                     
def game_loop():
    crashed = False
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
    passed = 0
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                crashed = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    delta_x = -5
                elif event.key == pygame.K_RIGHT:
                    delta_x = 5
                if event.key == pygame.K_UP:
                    delta_y = -5
                elif event.key == pygame.K_DOWN:
                    delta_y = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    delta_x = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    delta_y = 0
        random.shuffle(color)
        color_number = random.randrange(0 , 7)
        stuff_color = color[color_number]
        gameDisplay.blit( Bg , (0,0))
        x += delta_x
        y += delta_y
        print_score(passed)
        stuff(stuff_start_x , stuff_start_y ,stuff_width ,stuff_height ,stuff_color)
        stuff_start_y += stuff_speed
        plane(x , y)
        if x > display_width - plane_width or x < 0 :
            crash()
        if stuff_start_y > display_height :
            stuff_start_y = -stuff_height
            stuff_start_x = random.randrange(0 , display_width)
            passed += 1
        pygame.display.update()
        clock.tick(120)
        
#********** end def game_loop ()  ****************

        
game_loop()     
pygame.quit()
quit()
