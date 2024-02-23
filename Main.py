import pygame
import Constants as Const
import Map
import Player
pygame.init()

from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT
)


#Set up size of screen
screen = pygame.display.set_mode([Const.screenWidth,Const.screenHeight])

pygame.display.set_caption('Pac-man')

clock = pygame.time.Clock()

grid = Map.Grid()
player = Player.Player()

running = True

while running:
    for event in pygame.event.get():
        #stops the program when you close the window        
        if event.type == QUIT:
            running = False

    #check for user input
    pressed_keys = pygame.key.get_pressed()
    #updates the players position based on user input
    player.update(pressed_keys)
    #fills the background as black
    screen.fill((0,0,0))

    grid.drawPattern()

    # Render obstacles
    for obstacle in grid.obstacles:
        screen.blit(obstacle.image, obstacle.rect)
        
    #puts the player on the screen
    screen.blit(player.surf, player.rect)
    # sets the framerate
    clock.tick(30)
    #updates the screen
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()