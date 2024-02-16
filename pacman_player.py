# Pac-man Player
import pygame
from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

Screen_Width = 600
Screen_Height = 600

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
        self.surf.fill((255,255,0))
        self.rect = self.surf.get_rect()

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
        if self.rect.right > Screen_Width:
            self.rect.right = Screen_Width
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= Screen_Height:
            self.rect.bottom = Screen_Height
            
        
pygame.init()

# Set up the window
screen = pygame.display.set_mode([Screen_Width, Screen_Height])

player = Player()
#loops the gmae functions while the game is active
running = True

clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.type == K_ESCAPE:
                running = False
        #stops the program when you close the window        
        elif event.type == QUIT:
            running = False

    #check for user input
    pressed_keys = pygame.key.get_pressed()
    #updates the players position based on user input
    player.update(pressed_keys)
    #fills the background as black
    screen.fill((0,0,0))
    #puts the player on the screen
    screen.blit(player.surf, player.rect)
    # sets the framerate
    clock.tick(30)
    #updates the screen
    pygame.display.flip()


pygame.quit()