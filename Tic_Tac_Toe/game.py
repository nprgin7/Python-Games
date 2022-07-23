# Importing modules
import pygame, sys
import numpy as np


def input_type(row, col, player):
    board[row][col] = player
    
def check_board_field(row, col):
    if board[row][col] == 0:
        return True
    else:
        return False

def draw():
    for i in range(3):
        for j in range(3):
            if board[i][j] == 1:
                pygame.draw.circle( screen, LIGHT_GREY, (i * 200 + 100, j * 200 + 100), 60, 15)
            elif board[i][j] == 2:
                pygame.draw.line( screen, LIGHT_GREY, (i * 200 + 45, j * 200 + 200 - 45), (i * 200 + 200 - 45, j * 200 + 45), 25)
                pygame.draw.line( screen, LIGHT_GREY, (i * 200 + 45, j * 200 + 45), (i * 200 + 200 - 45, j * 200 + 200 - 45), 25)
    return True


def check_win(player):
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        draw_diagonal_winning_line(player)
        return True
    elif board[2][0] == player and board[1][1] == player and board[0][2] == player:
        draw_diagonal_winning_line(player, False)
        return True
        
    for col in range(3):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            draw_horizontal_winning_line(col, player)
            return True

    for row in range(3):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            draw_vertical_winning_line(row, player)
            return True

    return False

def draw_vertical_winning_line(col, player):
    posX = col * 200 + 200 / 2

    if player == 1:
        pygame.draw.line(screen, GREEN, (posX, 10), (posX, HEIGHT - 10), 15)
    else:
        pygame.draw.line(screen, GREEN, (posX, 10), (posX, HEIGHT - 10), 15)

def draw_horizontal_winning_line(row, player):
    posY = row * 200 + 200 / 2

    if player == 1:
        pygame.draw.line(screen, GREEN, (10, posY), (WIDTH - 10, posY), 15)

    else:
        pygame.draw.line(screen, GREEN, (10, posY), (WIDTH - 10, posY), 15)


def draw_diagonal_winning_line(player, down_diag=True):
    if down_diag:
        if player == 1:
            pygame.draw.line(screen, GREEN, (25, 25), (WIDTH - 25, HEIGHT - 25), 15)
        else:
            pygame.draw.line(screen, GREEN, (25, 25), (WIDTH - 25, HEIGHT - 25), 15)
    else:
        if player == 1:
            pygame.draw.line(screen, GREEN, (25, HEIGHT - 25), (WIDTH - 25, 25), 15)
        else:
            pygame.draw.line(screen, GREEN, (25, HEIGHT - 25), (WIDTH - 25, 25), 15)

def restart():
    screen.fill(GREY)
    pygame.draw.line( screen, LIGHT_GREY, (0, 200), (600, 200), 10 )
    pygame.draw.line( screen, LIGHT_GREY, (0, 400), (600, 400), 10 )

    pygame.draw.line( screen, LIGHT_GREY, (200, 0), (200, 600), 10 )
    pygame.draw.line( screen, LIGHT_GREY, (400, 0), (400, 600), 10 )
    
    for row in range(3):
        for col in range(3):
            board[row, col] = 0


pygame.init()
clock = pygame.time.Clock()

WIDTH, HEIGHT = 600, 600
GREY = (128, 128, 128)
LIGHT_GREY = (211, 211, 211)
GREEN = (50,205,50)

screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
pygame.display.set_caption( 'Tic Tac Toe' )
screen.fill(GREY)

pygame.draw.line( screen, LIGHT_GREY, (0, 200), (600, 200), 10 )
pygame.draw.line( screen, LIGHT_GREY, (0, 400), (600, 400), 10 )

pygame.draw.line( screen, LIGHT_GREY, (200, 0), (200, 600), 10 )
pygame.draw.line( screen, LIGHT_GREY, (400, 0), (400, 600), 10 )

board = np.zeros( (3, 3) )

game_over = False
player = 1

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                player = 1
                game_over = False
                restart()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            clickX, clickY = event.pos
            row, col = int(clickX // 200), int(clickY // 200)

            if check_board_field(row, col):
                if player == 1:
                    input_type(row, col, 1)
                    draw()
                    if check_win(player):
                        game_over = True
                    player = 2
                elif player == 2:
                    input_type(row, col, 2)
                    draw()
                    if check_win(player):
                        game_over = True
                    player = 1
                    
    pygame.display.update()
    clock.tick(60)
