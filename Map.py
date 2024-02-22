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
    def __init__(self, columns, rows, width):
        self.columns = 40
        self.rows = 60
        self.width = screenWidth / self.columns
      
    def draw(self):
      for i in range(self.columns):
        for j in range(self.rows):
         pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(i * self.width, j * self.width, self.width, self.width), 2)


#class Border(Fixed_object):
   # def __init__(self, colour):
      #  super().__init__(self.column, self.row)
       # self.colour = colour

    #def draw(self):
        


#class Obstacol(Fixed_object):
    #def __init__(self, colour):
       # super().__init__(column, row)
        #self.colour = colour



#class tunnel:

#class cage:
        