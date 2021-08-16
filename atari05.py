# pygame atari ver 5.0  By : M.H.Khademi
# Date: 99-11-20
import pygame
import time
pygame.init()
plane_width = 48
display_width = 800
display_height = 600
white = (255,255,255)
yellow = (255,255,100)
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


#********** def message_display ()  ****************

def message_display(text , size , color):
    largeText = pygame.font.Font('fonts\\Roboto-Black.ttf', size)
    TextSurf  = largeText.render(text , True , color)
    TextRect  = TextSurf.get_rect()
    TextRect.center = ((display_width/2) , (display_height/3))
    gameDisplay.blit(TextSurf , TextRect)
    pygame.display.update()
    time.sleep( 5 )
    game_loop ()

#********** def plane ()  ****************
    
def plane(x,y):
    gameDisplay.blit(planeimg , ( x , y))
    
#********** def crash ()  ****************
    
def crash():
    message_display( "You Crashed" , 100 , yellow)
                     
#********** def game_loop ()  ****************
                     
def game_loop(): 
    crashed = False
    x = display_width * 0.48
    y = display_height * 0.9
    delta_x = 0
    delta_y = 0
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
        gameDisplay.blit( Bg , (0,0))
        x += delta_x
        y += delta_y
        plane(x , y)
        if x > display_width - plane_width or x < 0 :
            crash()
        pygame.display.update()
        clock.tick(120)
        
#********** end def game_loop ()  ****************

        
game_loop()     
pygame.quit()
quit()
