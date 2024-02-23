# map class
import pygame

#Set up size of screen
screenWidth = 400
screenHeight = 576
screen = pygame.display.set_mode([screenWidth,screenHeight])
#Set up background
class Fixed_object:
    def __init__(self, columns, rows):
        self.column = columns
        self.row = rows



class Grid:

    obstacles = []

    def __init__(self):
        self.columns = 11
        self.rows = 9
        self.width = round(screenWidth / self.columns) 
        # Initializes map layout: 0 = empty space, 1 = obstacle
        # Refer to docs for map image
        self.array = [[0 for i in range(self.columns)],
                      [0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0],
                      [0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0],
                      [0, 0, 0, 0, 1, 1, 1, 0, 0 ,0 ,0],
                      [0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0],
                      [0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0],
                      [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
                      [0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0],
                      [0 for i in range(self.columns)]]
        self.createObstacles()
      
    def drawPattern(self):
        # Draws grid
        # offset for outer border
        for i in range(self.columns + 2):
            for j in range(self.rows + 2):
                # Screen, color, rectangle, border width
                pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(i * self.width, j * self.width, self.width, self.width), 1)
        self.drawBorder()


    def drawBorder(self):
        for i in range(self.columns + 2):
            y = i * self.width 
            for j in range(self.rows + 2):
                x = j * self.width
                if (i == 0 or i == self.columns + 1 or j == 0 or j == self.rows + 1): 
                    pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(i * self.width, j * self.width, self.width, self.width))
    def createObstacles(self):
        for i in range(self.columns):
            for j in range(self.rows):
                if (self.array[j][i] == 1):
                    self.obstacles.append(Obstacle(self.width, (i + 1) * self.width, (j + 1) * self.width))


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, width, x, y):
        super(Obstacle, self).__init__()
        self.image = pygame.Surface((width, width))
        self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect( topleft = (x,y))



#class tunnel:

#class cage:
        