import pygame
import player_class
pygame.init()


#Set up size of screen
screenWidth = 448
screenHeight = 576
screen = pygame.display.set_mode([screenWidth,screenHeight])

player = player_class.Player()

running = True

while running:
    
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #check for user input
    pressed_keys = pygame.key.get_pressed()
    #updates the players position based on user input
    player.update(pressed_keys)
    #fills the background as black
    screen.fill((0,0,0))
    #puts the player on the screen
    screen.blit(player.surf, player.rect)

# Done! Time to quit.
pygame.quit()