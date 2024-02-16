# Pac-man Player
import pygame
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

Screen_Width = 224
Screen_Height = 288

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
        self.surf = pygame.Surface((75,25))
        self.surf.fill((255,255,255))
        self.rect = self.surf.get_rect()

    def update(self):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)
        
pygame.init()

# Set up the window
screen = pygame.display.set_mode([Screen_Width, Screen_Height])

player = Player()

running = True

while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.type == K_ESCAPE:
                running = False
            
        
        elif event.type == QUIT:
            running = False


    pressed_keys = pygame.key.get_pressed

    player.update(pressed_keys)

    screen.fill((0,0,0))

    screen.blit(player.surf, player.rect)

    pygame.display.flip()


pygame.quit()