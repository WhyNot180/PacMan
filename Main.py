import math
import pygame
import Constants as Const
import Map
import Player
import Ghost
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

grid = Map.Grid(screen, Const.layout)
player = Player.Player()

# Enemy update group
enemySprites = pygame.sprite.Group()

collectables = pygame.sprite.Group()

pelletWidthOffset = (Const.gridRatio - collect.pellet.width)/2
pelletHeightOffset = (Const.gridRatio - collect.pellet.height)/2
for i in range(len(Const.layout[0])):
    for j in range(len(Const.layout)):
        if Const.layout[j][i] != 1:
            collect.pellet(i * Const.gridRatio + pelletWidthOffset, j * Const.gridRatio + pelletHeightOffset).add(collectables)
    

# Sprite rendering group
allSprites = pygame.sprite.Group()
allSprites.add(player)

blinky = Ghost.Ghost('red', Const.layout)
pinky = Ghost.Ghost('pink', Const.layout)
inky = Ghost.Ghost('blue', Const.layout)
clyde = Ghost.Ghost('orange', Const.layout)
enemySprites.add(blinky)
allSprites.add(blinky)
enemySprites.add(pinky)
allSprites.add(pinky)
enemySprites.add(inky)
allSprites.add(inky)
enemySprites.add(clyde)
allSprites.add(clyde)

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
    #fills the background as black
    screen.fill((0,0,0))

    grid.drawPattern()

    #updates the players position based on user input
    player.update(pressed_keys)

    for enemy in enemySprites:
        enemy.update(player.rect.y, player.rect.x, player.direction if player.direction > 0 else 1)
        if pygame.sprite.spritecollideany(enemy, grid.obstacles):
            enemy.rect.x = Const.gridRatio * round(enemy.rect.x/Const.gridRatio)
            enemy.rect.y = Const.gridRatio * round(enemy.rect.y/Const.gridRatio)
    
    if pygame.sprite.spritecollideany(player, grid.obstacles):
        player.direction = 0
        # Set player back to center of nearest tile
        player.rect.x = Const.gridRatio * round(player.rect.x/Const.gridRatio)
        player.rect.y = Const.gridRatio * round(player.rect.y/Const.gridRatio)
    
    collidingCollectables = pygame.sprite.spritecollide(player, collectables, True)
    for collectable in collidingCollectables:
        player.points += collectable.point_value
        print(player.points)

    #Render sprites
    for entity in allSprites:
        screen.blit(entity.surf, entity.rect)

    #TODO: Reset game
    if pygame.sprite.spritecollideany(player, enemySprites):
        player.kill()
        for enemy in enemySprites:
            enemy.direction = 0
    
    # sets the framerate
    clock.tick(20)
    #updates the screen
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()