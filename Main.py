import pygame
import Game
import Globals
pygame.init()

#Set up size of screen
screenWidth = 448
screenHeight = 576
screen = pygame.display.set_mode([screenWidth,screenHeight])

pacMan = Game.Game()

running = True

while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Starts game if and key is pressed
        elif event.type == pygame.KEYDOWN:
            Globals.GAMESTART = True
    
    # Fill the background with black
    screen.fill((0, 0, 0))
    
    if Globals.GAMESTART:
        pacMan.play()
    elif Globals.GAMEOVER or Globals.GAMEINIT:
        pacMan.reset()


    # Update the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()