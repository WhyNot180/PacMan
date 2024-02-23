# map class
import pygame

#Set up size of screen
screenWidth = 455
screenHeight = 576
screen = pygame.display.set_mode([screenWidth,screenHeight])

class Grid:

    obstacles = []

    def __init__(self):
        # Initializes map layout: 0 = empty space, 1 = obstacle
        # Refer to docs for map image
        self.array = [[1 for i in range(13)],
                      [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                      [1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
                      [1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
                      [1, 0, 0, 0, 0, 1, 1, 1, 0, 0 ,0 ,0, 1],
                      [1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
                      [1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
                      [1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1],
                      [1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1],
                      [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                      [1 for i in range(13)]]
        
        self.rows = len(self.array)
        self.columns = len(self.array[0])

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
                if (self.array[j][i] == 1):
                    self.obstacles.append(Obstacle(self.width, i * self.width, j * self.width))


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, width, x, y):
        super(Obstacle, self).__init__()
        self.image = pygame.Surface((width, width))
        self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect( topleft = (x,y))
        