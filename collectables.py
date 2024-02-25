import pygame

class collectables(pygame.sprite.Sprite):

  width = 15
  height = 15

  def __init__(self, position_x, position_y):
    super().__init__()
    self.surf = pygame.Surface([self.width, self.height])
    self.rect = self.surf.get_rect()
    self.position_x = position_x
    self.position_y = position_y
    self.rect.x = position_x
    self.rect.y = position_y

class pellet(collectables):
   point_value = 10
   def __init__(self, position_x, position_y):
     super().__init__(position_x, position_y)
     self.surf.fill((255, 255, 255)) 

class power_pellet(collectables):
    point_value = 50
    def __init__ (self, position_x, position_y):
      super(). __init__ (position_x, position_y)
      self.surf.fill((0, 200, 0))

class fruit(collectables):
    point_value = 100
    def __init__ (self, position_x, position_y):
      super(). __init__ (position_x, position_y)
      self.surf.fill((0, 0, 200))