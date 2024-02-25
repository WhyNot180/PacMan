# Player class
import pygame
import Globals 

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT
)

class Player(pygame.sprite.Sprite):
    lives = 3
    points = 0
    powered_up = False
    spawn_x = 0
    spawn_y = 0
    # 1 is right
    # 2 is left
    # 3 is up
    # 4 is down
    direction = 0
    speed = 5

    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((Globals.gridRatio,Globals.gridRatio))
        self.surf.fill((196,180,0))
        self.rect = self.surf.get_rect(topleft = (6*Globals.gridRatio, 6*Globals.gridRatio))

    def update(self, pressed_keys):
        # Changes the direction the player is looking
        if pressed_keys[K_UP]:
            self.direction = 4
        if pressed_keys[K_DOWN]:
            self.direction = 3
        if pressed_keys[K_LEFT]:
            self.direction = 2
        if pressed_keys[K_RIGHT]:
            self.direction = 1

        # Move player in direction they are looking
        if self.direction == 1:
            self.rect.move_ip(self.speed, 0)
        if self.direction == 2:
            self.rect.move_ip(-self.speed, 0)
        if self.direction == 3:
            self.rect.move_ip(0, self.speed)
        if self.direction == 4:
            self.rect.move_ip(0, -self.speed)

        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > Globals.screenWidth:
            self.rect.right = Globals.screenWidth
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= Globals.screenHeight:
            self.rect.bottom = Globals.screenHeight