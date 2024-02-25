# map class
import pygame
import Constants as Const

class Grid:

    obstacles = []

    def __init__(self, screen, layout):
        
        self.screen = screen
        self.layout = layout
        
        self.rows = len(self.layout)
        self.columns = len(self.layout[0])

        self.width = round(Const.screenWidth / self.columns) 
        
        self.createObstacles()
      
    def drawPattern(self):
        # Draws grid
        # offset for outer border
        for i in range(self.columns):
            for j in range(self.rows):
                # Screen, color, rectangle, border width
                pygame.draw.rect(self.screen, (0, 0, 255), pygame.Rect(i * self.width, j * self.width, self.width, self.width), 1)
    
    def createObstacles(self):
        for i in range(self.columns):
            for j in range(self.rows):
                if (self.layout[j][i] == 1):
                    self.obstacles.append(Obstacle(self.width, i * self.width, j * self.width))


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, width, x, y):
        super(Obstacle, self).__init__()
        self.surf = pygame.Surface((width, width))
        self.surf.fill((0, 0, 255))
        self.rect = self.surf.get_rect( topleft = (x,y))
        