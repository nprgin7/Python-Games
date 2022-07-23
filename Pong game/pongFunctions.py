import pygame

def set_background(screen, width, height, background_color, line_color):
    screen.fill(background_color)
    pygame.draw.line(screen, line_color, (width // 2 , 0), (width // 2, height), 5 )

def ballPlayer1( Ball, PlayerObject):
    if Ball.posY + Ball.radius > PlayerObject.posY and Ball.posY - Ball.radius < PlayerObject.posY + PlayerObject.height:
        if Ball.posX - Ball.radius <= PlayerObject.posX + PlayerObject.width:
            return True
    return False

def ballPlayer2( Ball, PlayerObject):
    if Ball.posY + Ball.radius > PlayerObject.posY and Ball.posY - Ball.radius < PlayerObject.posY + PlayerObject.height:
        if Ball.posX + Ball.radius >= PlayerObject.posX:
            return True
    return False

def ballWalls( Ball, screen):

    if Ball.posY - Ball.radius <= 0:
        return True
    
    if Ball.posY + Ball.radius >= screen.get_height():
        return True
    
    return False

def player1Scored( Ball, width ):
    return Ball.posX - Ball.radius >= width
    
def player2Scored( Ball ):
    return Ball.posX - Ball.radius <= 0