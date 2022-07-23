# Importing modules
import pygame, sys  

pygame.init()
clock = pygame.time.Clock()
my_font = pygame.font.SysFont('Comic Sans MS', 60)

WIDTH, HEIGHT = 600, 600
GREY = (128, 128, 128)

RED = (255, 0, 0)
BLUE = (0, 0, 255)

screen = pygame.display.set_mode( (WIDTH, HEIGHT) )
pygame.display.set_caption( 'Fast Fingers' )
screen.fill(GREY)


p1 = 10
p2 = 590
pygame.draw.line( screen, RED, (0, 300), (p1, 300), 40 )
pygame.draw.line( screen, BLUE, (600, 300), (p2, 300), 40)

game_over = False
# Game loop
while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LCTRL and not game_over:
                p1 += 10
                pygame.draw.line( screen, RED, (0, 300), (p1, 300), 40 )
                pygame.draw.line( screen, BLUE, (600, 300), (p2, 300), 40)
            if event.key == pygame.K_RCTRL and not game_over:
                p2 -= 10
                screen.fill(GREY)
                pygame.draw.line( screen, RED, (0, 300), (p1, 300), 40 )
                pygame.draw.line( screen, BLUE, (600, 300), (p2, 300), 40)
            if event.key == pygame.K_r:
                p1 = 0
                p2 = 600
                screen.fill(GREY)
                pygame.draw.line( screen, RED, (0, 300), (p1, 300), 40 )
                pygame.draw.line( screen, BLUE, (600, 300), (p2, 300), 40)
                game_over = False
            if p1 == 300:
                game_over = True
                screen.blit(my_font.render('Red Wins', True, (0, 0, 0)), (0,0))
            if p2 == 300:
                game_over = True
                screen.blit(my_font.render('Blue Wins', True, (0, 0, 0)), (0,0))
        
    pygame.display.update()
    clock.tick(60)

