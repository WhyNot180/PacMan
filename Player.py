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
    x_position = 0
    y_position = 0
    # orientation in gradians i.e. up is 4, left is 1, down is 2, right is 3
    direction = 1

    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((25,25))
        self.surf.fill((196,180,0))
        self.rect = self.surf.get_rect()
        self.rect.move_ip(Const.screenWidth/2, Const.screenHeight/2)

    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > Const.screenWidth:
            self.rect.right = Const.screenWidth
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= Const.screenHeight:
            self.rect.bottom = Const.screenHeight