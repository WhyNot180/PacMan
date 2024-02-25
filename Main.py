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
    elif Globals.GAMEOVER or Globals.GAMEINIT:
        pacMan.reset()
    
    # sets the framerate
    clock.tick(20)
    #updates the screen
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()