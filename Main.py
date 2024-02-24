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

# Initializes map layout: 0 = empty space, 1 = obstacle
# Refer to docs for map image
layout = [[1 for i in range(13)],
                      [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                      [1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
                      [1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
                      [1, 0, 0, 0, 0, 1, 1, 1, 0, 0 ,0 ,0, 1],
                      [1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
                      [1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
                      [1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1],
                      [1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1],
                      [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                      [1 for i in range(13)]]

grid = Map.Grid(layout)
player = Player.Player()

collectables = pygame.sprite.Group()
for i in range(len(layout[0])):
    for j in range(len(layout)):
        if layout[j][i] == 0:
            collect.pellet(i * Const.screenWidth/13 + (Const.screenWidth/13 - 15)/2, j * Const.screenWidth/13 + (Const.screenWidth/13 - 15)/2).add(collectables)
    

# Sprite rendering group
allSprites = pygame.sprite.Group()
allSprites.add(player)
for collectable in collectables:
    allSprites.add(collectable)
for obstacle in grid.obstacles:
    allSprites.add(obstacle)

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

    if pygame.sprite.spritecollideany(player, grid.obstacles):
        player.direction = 0
        player.rect.x = 35 * round(player.rect.x/35)
        player.rect.y = 35 * round(player.rect.y/35)
    
    collidingCollectables = pygame.sprite.spritecollide(player, collectables, True)
    for collectable in collidingCollectables:
        player.points += collectable.point_value
        print(player.points)

    #Render sprites
    for entity in allSprites:
        screen.blit(entity.surf, entity.rect)
    
    # sets the framerate
    clock.tick(20)
    #updates the screen
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()