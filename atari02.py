# pygame atari ver 2.0  By : M.H.Khademi
# Date: 99-11-07
import pygame
pygame.init()
display_width = 800
display_height = 600
white = (255,255,255)
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

#********** def plane ()  ****************
def plane(x,y):
    gameDisplay.blit(planeimg , ( x , y))
        
 
crashed = False
x = display_width * 0.48
y = display_height * 0.9
while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

    plane(x , y)
    pygame.display.update()
    clock.tick(120)
pygame.quit()
quit()
