import sys

import pygame
from pygame.locals import QUIT

pygame.init()
DISPLAYSURF = pygame.display.set_mode((500, 500))
DISPLAYSURF.fill((255, 255, 255))

class collectables(pygame.sprite.Sprite, pygame.sprite.Group):
  def __init__(self, position_x, position_y, point_value):
    super().__init__()
    self.image = pygame.Surface([25, 25])
    self.image.fill((0, 0, 0))
    self.rect = self.image.get_rect()
    self.position_x = position_x
    self.position_y = position_y
    self.point_value = point_value
    self.rect.x = position_x
    self.rect.y = position_y

test = collectables(50, 100, 10)
test2 = collectables(100, 100, 10)

class pellet(collectables):
   def __init__ (self, position_x, position_y, point_value):
     super().__init__(position_x, position_y, point_value)
     self.image.fill((200, 0, 0))
     self.point_value = 10
     self.level_up = False 
     self.spawn_fruit = False

test3 = pellet(150, 100, 10)

class power_pellet(collectables):
    def __init__ (self, position_x, position_y, point_value):
      super(). __init__ (position_x, position_y, point_value)
      self.image.fill((0, 200, 0))
      self.point_value = 50
      self.power_up = False

test4 = power_pellet(200, 100, 10)

class fruit(collectables):
    def __init__ (self, fruit_type, position_x, position_y, point_value):
      super(). __init__ (position_x, position_y, point_value)
      self.image.fill((0, 0, 200))
      self.fruit_type = fruit_type
      self.point_value = 100
      self.appear = False

test5 = fruit("cherry", 250, 100, 10)
print(test5.fruit_type)

all_sprites = pygame.sprite.Group()
all_sprites.add(test, test2, test3, test4, test5)
for entity in all_sprites:
  DISPLAYSURF.blit(entity.image, entity.rect)

pygame.display.set_caption('Hello World!')
while True:
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
  
  pygame.display.flip()
  pygame.display.update()
