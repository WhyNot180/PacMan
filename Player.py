# Player class
import pygame
import Constants as Const

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
    # orientation in gradians i.e. up is 4, right is 1, down is 2, left is 3
    direction = 0

    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((Const.screenWidth/13,Const.screenWidth/13))
        self.surf.fill((196,180,0))
        self.rect = self.surf.get_rect(topleft = (6*(Const.screenWidth/13), 6*(Const.screenWidth/13)))

    def update(self, pressed_keys):
        # Changes the direction the player is looking
        if pressed_keys[K_UP]:
            self.direction = 4
        if pressed_keys[K_DOWN]:
            self.direction = 2
        if pressed_keys[K_LEFT]:
            self.direction = 3
        if pressed_keys[K_RIGHT]:
            self.direction = 1

        # Move player in direction they are looking
        if self.direction == 1:
            self.rect.move_ip(5, 0)
        if self.direction == 2:
            self.rect.move_ip(0, 5)
        if self.direction == 3:
            self.rect.move_ip(-5, 0)
        if self.direction == 4:
            self.rect.move_ip(0, -5)

        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > Const.screenWidth:
            self.rect.right = Const.screenWidth
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= Const.screenHeight:
            self.rect.bottom = Const.screenHeight