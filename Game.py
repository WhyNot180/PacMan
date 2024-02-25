import pygame
import Globals

class Game:
    lives = 3

    def __init__(self):
        self.reset()

    def reset(self):
        print("Reseting everything!")

        print("Resetting player position")
        print("Resetting enemy positions")
        print("Resetting collectables")
        print("Resetting points")
        print("Resetting level")
        self.lives = 3
        Globals.GAMEINIT = False
        Globals.GAMEOVER = False


    def play(self):
        enemyCollision = True
        collectableCollision = True
        collectables = 1
        
        print("Updating player position")
        print("Updating enemy position")

        print("Checking for collisions between movable entity and walls")

        print("Checking for collisions between enemy and player")
        if enemyCollision:
            self.lives -= 1
            print("Decreasing lives")
            print(self.lives)
            if self.lives <= 0:
                print("No lives")
                Globals.GAMESTART = False
                Globals.GAMEOVER = True
        print("Checking for collisions between player and collectables")
        if collectableCollision: 
            collectables -= 1
            print("Adding points...")
        if collectables == 0:
            print("Increasing level...")
            print("Resetting collectables")
            collectables = 1
        