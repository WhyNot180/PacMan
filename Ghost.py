import pygame
import random

class Ghost(pygame.sprite.Sprite):

    isScared : bool

    def __init__(self, colour):
        super(Ghost, self).__init__()
        self.surf = pygame.Surface((20,10))
        self.surf.fill((255,255,255))
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )
        self.speed = random.randint(5, 20)
        self.colour = colour
    # Move the sprite based on speed
    # Remove the sprite when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()
    
    def scared():
        isScared = True