import math
import pygame
import Game
import Globals
import Globals 
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
screen = pygame.display.set_mode([Globals.screenWidth,Globals.screenHeight])

pygame.display.set_caption('Pac-man')

clock = pygame.time.Clock()

pacMan = Game.Game(screen)

running = True

font = pygame.font.SysFont('arial', 32)

gameOverText = font.render('Game Over', True, (255, 0, 0))

pressPlayText = font.render('Press Any Button To Start', True, (0, 255, 0))

gameOverTextRect = gameOverText.get_rect()
pressPlayTextRect = pressPlayText.get_rect()

gameOverTextRect.topleft = (50, 400)
pressPlayTextRect.topleft = (50, 450)

# Initialize
screen.blit(pressPlayText, pressPlayTextRect)
pacMan.reset()

while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        #stops the program when you close the window        
        if event.type == QUIT:
            running = False
        # Starts game if and key is pressed
        elif event.type == pygame.KEYDOWN:
            Globals.GAMESTART = True
    #check for user input
    pressed_keys = pygame.key.get_pressed()

    if Globals.GAMESTART:
        pacMan.play(pressed_keys)
    elif Globals.GAMEOVER:
        screen.blit(gameOverText, gameOverTextRect)
        screen.blit(pressPlayText, pressPlayTextRect)
        pacMan.reset()
    
    # sets the framerate
    clock.tick(20)
    #updates the screen
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()