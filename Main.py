import pygame
import Map
pygame.init()

#Set up size of screen
screenWidth = 448
screenHeight = 576
screen = pygame.display.set_mode([screenWidth,screenHeight])
grid = Map.Grid(40,60,screenWidth / 40)
running = True


while running:
    
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((0, 0, 0))
    grid.draw()
    # Draw a solid blue circle in the center

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()