import math
import pygame
import Constants as Const
import Map
import Player
import collectables as collect
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
pellet = collect.pellet(50,50)

# Sprite rendering group
allSprites = pygame.sprite.Group()
allSprites.add(player)
allSprites.add(pellet)



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
    
    if pygame.sprite.spritecollideany(player, grid.obstacles):
        player.direction = 0
        player.rect.x = 35 * round(player.rect.x/35)
        player.rect.y = 35 * round(player.rect.y/35)
        
    #puts the player on the screen
    for entity in allSprites:
        screen.blit(entity.surf, entity.rect)
    # sets the framerate
    clock.tick(20)
    #updates the screen
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()