import pygame
import Globals
import Player
import Map
import Ghost
import collectables as collect

class Game:
    
    player : Player.Player 

    # Enemy update group
    enemySprites = pygame.sprite.Group()

    collectables = pygame.sprite.Group()
    
    # Sprite rendering group
    allSprites = pygame.sprite.Group()

    def __init__(self, screen):
        self.screen = screen
        self.grid = Map.Grid(self.screen, Globals.layout)
        
        self.reset()

    def reset(self):

        # Empty all sprite groups
        self.allSprites.empty()
        self.collectables.empty()
        self.enemySprites.empty()

        # Reset player
        self.player = Player.Player()

        self.allSprites.add(self.player)
        
        # Reset collectables
        pelletWidthOffset = (Globals.gridRatio - collect.pellet.width)/2
        pelletHeightOffset = (Globals.gridRatio - collect.pellet.height)/2

        for i in range(len(Globals.layout[0])):
            for j in range(len(Globals.layout)):
                if Globals.layout[j][i] != 1:
                    collect.pellet(i * Globals.gridRatio + pelletWidthOffset, j * Globals.gridRatio + pelletHeightOffset).add(self.collectables)
        
        for collectable in self.collectables:
            self.allSprites.add(collectable)

        # Reset enemies
        blinky = Ghost.Ghost('red', Globals.layout)
        pinky = Ghost.Ghost('pink', Globals.layout)
        inky = Ghost.Ghost('blue', Globals.layout)
        clyde = Ghost.Ghost('orange', Globals.layout)

        self.enemySprites.add(blinky)
        self.allSprites.add(blinky)

        self.enemySprites.add(pinky)
        self.allSprites.add(pinky)

        self.enemySprites.add(inky)
        self.allSprites.add(inky)

        self.enemySprites.add(clyde)
        self.allSprites.add(clyde)

        
        # Reset map obstacles
        for obstacle in self.grid.obstacles:
            self.allSprites.add(obstacle)

        Globals.GAMEINIT = False
        Globals.GAMEOVER = False

    def __updateSprites(self, pressed_keys):

        #updates the players position based on user input
        self.player.update(pressed_keys)

        for enemy in self.enemySprites:
            enemy.update(self.player.rect.y, self.player.rect.x)
            if pygame.sprite.spritecollideany(enemy, self.grid.obstacles):
                enemy.rect.x = Globals.gridRatio * round(enemy.rect.x/Globals.gridRatio)
                enemy.rect.y = Globals.gridRatio * round(enemy.rect.y/Globals.gridRatio)
        
        if pygame.sprite.spritecollideany(self.player, self.grid.obstacles):
            self.player.direction = 0
            # Set player back to center of nearest tile
            self.player.rect.x = Globals.gridRatio * round(self.player.rect.x/Globals.gridRatio)
            self.player.rect.y = Globals.gridRatio * round(self.player.rect.y/Globals.gridRatio)
        
        collidingCollectables = pygame.sprite.spritecollide(self.player, self.collectables, True)
        for collectable in collidingCollectables:
            self.player.points += collectable.point_value
            print(self.player.points)
        
        if pygame.sprite.spritecollideany(self.player, self.enemySprites):
            Globals.GAMESTART = False
            Globals.GAMEOVER = True

    def __render(self):

        #fills the background as black
        self.screen.fill((0,0,0))

        self.grid.drawPattern()

        #Render sprites
        for entity in self.allSprites:
            self.screen.blit(entity.surf, entity.rect)


    def play(self, pressed_keys):

        self.__render()

        self.__updateSprites(pressed_keys)
        