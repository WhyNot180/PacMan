import pygame
import random
import Constants as Const

class Ghost(pygame.sprite.Sprite):

    isScared : bool
    direction : int

    def __init__(self, colour):
        super(Ghost, self).__init__()
        self.surf = pygame.Surface((25,25))
        self.surf.fill((255,255,255))
        self.rect = self.surf.get_rect(
            center=(
                random.randint(Const.screenWidth + 20, Const.screenWidth + 100),
                random.randint(0, Const.screenHeight),
            )
        )
        self.speed = 5
        self.colour = colour
    # Move the sprite based on speed
    # Remove the sprite when it passes the left edge of the screen
    def update(self, playerRight):
        
        if self.rect.right < playerRight:
            self.direction = 1
        elif self.rect.right > playerRight:
            self.direction = 2
        else:
            self.direction = 0
        
        if self.direction == 1:
            self.rect.move_ip(self.speed, 0)
        elif self.direction == 2:
            self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()
    
    def scared(self):
        self.isScared = True