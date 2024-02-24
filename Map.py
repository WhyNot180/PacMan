# map class
import pygame

#Set up size of screen
screenWidth = 455
screenHeight = 576
screen = pygame.display.set_mode([screenWidth,screenHeight])

class Grid:

    obstacles = []

    def __init__(self, layout):
        
        self.layout = layout
        
        self.rows = len(self.layout)
        self.columns = len(self.layout[0])

        self.width = round(screenWidth / self.columns) 
        
        self.createObstacles()
      
    def drawPattern(self):
        # Draws grid
        # offset for outer border
        for i in range(self.columns):
            for j in range(self.rows):
                # Screen, color, rectangle, border width
                pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(i * self.width, j * self.width, self.width, self.width), 1)
    
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
        