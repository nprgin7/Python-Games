# Importing modules
import pygame, sys, pongFunctions
from gameClasses import Ball, PlayerObject, ScoreCard

pygame.init()
clock = pygame.time.Clock()

# Initializing global variables
WIDTH = 900
HEIGHT = 500

BLACK = (0,0,0)
WHITE = (255, 255, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill((0, 0, 0))
pygame.display.set_caption("Pong")

pongFunctions.set_background(screen, WIDTH, HEIGHT, BLACK, WHITE)

ball = Ball(screen, WHITE, WIDTH // 2, HEIGHT // 2, 15)

player1 = PlayerObject(screen, WHITE, 15,  HEIGHT // 2 - 60, 20, 120)
player2 = PlayerObject(screen, WHITE, WIDTH - 35,  HEIGHT // 2 - 60, 20, 120)

scorePlayer1 = ScoreCard(screen, '0', WIDTH // 4, 15, WHITE)
scorePlayer2 = ScoreCard(screen, '0', WIDTH - WIDTH // 4, 15, WHITE)
run = False

# Game loop

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                ball.movement_start()
                run = True

            if event.key == pygame.K_w:
                player1.move_option = 'UP'
            if event.key == pygame.K_s:
                player1.move_option = 'DOWN'

            if event.key == pygame.K_UP:
                player2.move_option = 'UP'
            if event.key == pygame.K_DOWN:
                player2.move_option = 'DOWN'

        if event.type == pygame.KEYUP:
            player1.move_option, player2.move_option = 'STOP', 'STOP'

    if run:
        pongFunctions.set_background(screen, WIDTH, HEIGHT, BLACK, WHITE)
        
        ball.movement()
        ball.create()

        player1.movement()
        player1.border_colider()
        player1.create()

        player2.movement()
        player2.border_colider()
        player2.create()

        if pongFunctions.ballPlayer1(ball, player1):
            ball.player_collison()
        if pongFunctions.ballPlayer2(ball, player2):
            ball.player_collison()
        if pongFunctions.ballWalls(ball, screen):
            ball.wall_collison()

        if pongFunctions.player1Scored(ball, WIDTH):
            scorePlayer1.addPoint()
            ball.restart_movement()
            player1.restart_movement()
            player2.restart_movement()
            
        if pongFunctions.player2Scored(ball):
            scorePlayer2.addPoint()
            ball.restart_movement()
            player1.restart_movement()
            player2.restart_movement()

    scorePlayer1.create()
    scorePlayer2.create()

    pygame.display.update()
    clock.tick(60)