import pygame, sys

pygame.init()

black = (   0,    0,    0)
white = ( 255,  255,  255)
red   = ( 255,    0,    0)
screen_size=(800,600)

player_width = 15
player_heigt = 90 

screen=pygame.display.set_mode(screen_size)
clock=pygame.time.Clock()

#Coordinates and speed of player 1
player1_x_coor=50 
player1_y_coor=300 - (player_heigt / 2)
player1_y_speed=0 

#Coordinates and speed of player 2
player2_x_coor=750-player_width 
player2_y_coor=300 - (player_heigt / 2)
player2_y_speed=0 

game_over = False

#Coordinates of the ball 
ball_x = 400
ball_y = 300
speed_ball_x = 3
speed_ball_y = 3



while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over=True

        if event.type == pygame.KEYDOWN:
            #Player 1
            if event.key == pygame.K_w:
                player1_y_speed =-3

            if event.key == pygame.K_s:
                player1_y_speed =3

            #player 2
            if event.key == pygame.K_UP:
                player2_y_speed =-3

            if event.key == pygame.K_DOWN:
                player2_y_speed =3      

        if event.type == pygame.KEYUP:
            #Player 1
            if event.key == pygame.K_w:
                player1_y_speed =0

            if event.key == pygame.K_s:
                player1_y_speed =0

            #player 2
            if event.key== pygame.K_UP:
                player2_y_speed =0

            if event.key == pygame.K_DOWN:
                player2_y_speed =0        


    #Modify the coordinates to give movement to the players and the ball
    
    player1_y_coor += player1_y_speed
    player2_y_coor += player2_y_speed

    # Barreras del Jugador 1
    if player1_y_coor < 0:
        player1_y_coor = 0  
    if player1_y_coor > 510:
        player1_y_coor = 510

    # Barreras del Jugador 2
    if player2_y_coor < 0:
        player2_y_coor = 0
    if player2_y_coor > 510:
        player2_y_coor = 510






    screen.fill(black)
    #Drawing zone

    player1 = pygame.draw.rect(screen,white,(player1_x_coor,player1_y_coor,player_width,player_heigt))
    player2 = pygame.draw.rect(screen,white,(player2_x_coor,player2_y_coor,player_width,player_heigt))
    pygame.draw.circle(screen,white,(ball_x,ball_y),10)    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()