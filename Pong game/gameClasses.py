import pygame

class Ball:
    def __init__(self, screen, color, posX, posY, radius):
        self.screen = screen
        self.color = color
        self.posX = posX
        self.posY = posY
        self.radius = radius

        self.dirX = 0
        self.dirY = 0

        self.create()

    def create(self):
        pygame.draw.circle (self.screen, self.color, (self.posX, self.posY), self.radius)

    def movement_start(self):
        self.dirX = 6
        self.dirY = 2

    def movement(self):
        self.posX = self.dirX + self.posX
        self.posY = self.dirY + self.posY

    def player_collison(self):
        self.dirX = -self.dirX

    def wall_collison(self):
        self.dirY = -self.dirY

    def restart_movement(self):
        self.posX = self.screen.get_width() // 2
        self.posY = self.screen.get_height() // 2
        self.dirX = 0
        self.dirY = 0
        self.create()

class PlayerObject:
    def __init__(self, screen, color, posX, posY, width, height):
        self.screen = screen
        self.color = color
        self.posX = posX
        self.posY = posY
        self.width = width
        self.height = height

        self.move_option = 'None'

        self.create()

    def create(self):
        pygame.draw.rect(self.screen, self.color, (self.posX, self.posY, self.width, self.height))

    def movement(self):
        if self.move_option == 'UP':
            self.posY -= 10
        elif self.move_option == 'DOWN':
            self.posY += 10

    def border_colider(self):
        if self.posY <= 0:
            self.posY = 0
        if self.posY >= (self.screen.get_height() - self.height):
            self.posY = self.screen.get_height() - self.height

    def restart_movement(self):
        self.posY = self.screen.get_height() // 2 - self.height // 2
        self.move_option = 'none'
        self.create()

class ScoreCard:
    def __init__(self, screen, points, posX, posY, color):
        self.screen = screen
        self.points = points
        self.posX = posX
        self.posY = posY
        self.color = color
        self.font = pygame.font.SysFont("monospace", 80, bold=True)
        self.label = self.font.render(self.points, 0, self.color)

        self.create()
    
    def create(self):
        self.screen.blit(self.label, (self.posX - self.label.get_rect().width // 2, self.posY))

    def addPoint(self):
        self.points = str(int(self.points) + 1)
        self.label = self.font.render(self.points, 0, self.color)
