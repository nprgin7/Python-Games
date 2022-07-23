# Importing modules
import pygame, sys

WIDTH, HEIGHT = 700, 700
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

pygame.init()
screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
pygame.display.set_caption( 'Connect 4' )
my_font = pygame.font.SysFont('Comic Sans MS', 60)

board = [[0, 0, 0, 0, 0, 0, 0,], 
         [0, 0, 0, 0, 0, 0, 0,], 
         [0, 0, 0, 0, 0, 0, 0,], 
         [0, 0, 0, 0, 0, 0, 0,], 
         [0, 0, 0, 0, 0, 0, 0,], 
         [0, 0, 0, 0, 0, 0, 0,], 
         [0, 0, 0, 0, 0, 0, 0,]]

def draw_board():
    screen.fill(BLUE)
    for i in range(7):
        for j in range(7):
            pygame.draw.circle(screen, WHITE, (i*100 + 50, j*100 + 50) , 45, 100)


def check_win():
    for i in range(4):
        for j in range(4):
            if board[i][j] == board[i + 1][j + 1] == board[i + 2][j + 2] == board[i + 3][j + 3] != 0:
                 return True
            
        for z in range(7):
            if board[i][z] == board[i + 1][z] == board[i + 2][z] == board[i + 3][z] != 0:
                return True

    for i in range(7):
        for j in range(4):
            if board[i][j] == board[i][j + 1] == board[i][j + 2] == board[i][j + 3] != 0:
                return True

    for i in range(6, 2, -1):
        for j in range(4):
            if board[j][i] == board[j + 1][i - 1] == board[j + 2][i - 2] == board[j + 3][i - 3] != 0:
                return True


def draw_cricle(col, row, player):

    global board

    if player == 1:
        color = RED
    elif player == 2:
        color = YELLOW

    for i in range(6, -1, -1):
        if board[i][col] == 0:
            pygame.draw.circle(screen, color, (col*100 + 50, i*100 + 50) , 45, 100)
            board[i][col] = player
            break    

draw_board()

player = 1

pygame.init()
clock = pygame.time.Clock()
game_over = False

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            clickX, clickY = event.pos
            col, row = int(clickX // 100), int(clickY // 100)
            draw_cricle(col, row, player)
            if(check_win()):
                if player == 1:
                    screen.blit(my_font.render('Red Wins', True, (0, 0, 0)), (0,0))
                if player == 2:
                    screen.blit(my_font.render('Yellow Wins', True, (0, 0, 0)), (0,0))
                game_over = True
            if player == 1:
                player = 2
            else:
                player = 1
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    player = 1
                    board = [[0, 0, 0, 0, 0, 0, 0,], 
                            [0, 0, 0, 0, 0, 0, 0,], 
                            [0, 0, 0, 0, 0, 0, 0,], 
                            [0, 0, 0, 0, 0, 0, 0,], 
                            [0, 0, 0, 0, 0, 0, 0,], 
                            [0, 0, 0, 0, 0, 0, 0,], 
                            [0, 0, 0, 0, 0, 0, 0,]]
                    draw_board()
                    game_over = False

    pygame.display.update()
    clock.tick(60)