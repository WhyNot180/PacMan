import sys

import pygame
from pygame.locals import QUIT

pygame.init()
DISPLAYSURF = pygame.display.set_mode((500, 500))
DISPLAYSURF.fill((255, 255, 255))

class collectables(pygame.sprite.Sprite):
  def __init__(self, position_x, position_y, point_value):
    super().__init__()
    self.image = pygame.Surface([50, 50])
    self.image.fill((111, 0, 0))
    self.rect = self.image.get_rect()
    self.position_x = position_x
    self.position_y = position_y
    self.point_value = point_value

test = collectables(100, 100, 10)
test2 = collectables(200, 200, 10)

#class pellet(collectables):
#      super(). __init__ (position_x, position_y, point_value)
#      self.point_value = 10
#      self.level_up = False
#      self.spawn_fruit = False

#class power_pellet(collectables):
#    def __init__ (self, position_x, position_y, point_value):
#      super(). __init__ 
#      self.point_value = 50
#      self.power_up = False

#class fruit(collectables):
#    def __init__ (self, position_x, position_y, point_value):
#      super(). __init__ 
#      self.point_value = 100
#      self.appear = False
#      pass

pygame.display.set_caption('Hello World!')
while True:
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
      test.draw()
  DISPLAYSURF.blit(test.image, test.rect)
  pygame.display.flip()
  #pygame.display.update()
