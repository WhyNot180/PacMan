import pygame
import Constants as Const
import Player
import Ghost
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

player = Player.Player()


# Enemy update group
enemySprites = pygame.sprite.Group()

# Sprite rendering group
allSprites = pygame.sprite.Group()
allSprites.add(player)
for x in range(5):
    ghost = Ghost.Ghost((255,255,255))
    enemySprites.add(ghost)
    allSprites.add(ghost)

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
    for enemy in enemySprites:
        enemy.update(player.rect.right)
    #fills the background as black
    screen.fill((0,0,0))
    #puts the player on the screen
    for entity in allSprites:
        screen.blit(entity.surf, entity.rect)

    if pygame.sprite.spritecollideany(player, enemySprites):
        player.kill()
    # sets the framerate
    clock.tick(30)
    #updates the screen
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()