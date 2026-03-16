import pygame, sys

#define colors (RED,GREEN,BLUE)

BLACK=(   0,   0,   0) 
WHITE=( 255, 255, 255)
GREEN=(   0, 255, 0)
RED  =( 255,   0,   0) 
BLUE =(   0,   0, 255)


pygame.init()

size = (800, 500)
screen = pygame.display.set_mode(size)          #Create a window
clock = pygame.time.Clock()                     #Control FPS



#coordinates of the square
cord_x = 400
cord_y = 200 

#speed at which the square will move
speed_x = 2
speed_y = 3



while True:                                     #The lines 8-12 is the most basic thing for de program
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    if (cord_x> 720 or cord_x< 0):
        speed_x*=-1
    if (cord_y> 420 or cord_y< 0):
        speed_y*=-1

    cord_x+=speed_x
    cord_y+=speed_y
    screen.fill(WHITE)                          #Backgraund colors
    #### ------Drawing zone 

    #pygame.draw.line(screen,GREEN,[0,100],[200,300],5)         #These are examples of how to draw circles, lines, and rectangles.
    #pygame.draw.rect(screen, BLACK,(100,100,80,80))
    #pygame.draw.circle(screen,BLACK,(200,200),30)

    #for x in range(100,700,100):                               #This is a example of how to draw a sequency of figures whit a loop (bucle) 
    #    pygame.draw.rect(screen,BLACK,(x,230,50,50))
    #    pygame.draw.line(screen,GREEN,(x,0),(x,100),5)


    pygame.draw.rect(screen,RED,(cord_x,cord_y,80,80))
    #### ------Drawing zone  
    pygame.display.flip()                       #Refresh screen
    clock.tick(60)