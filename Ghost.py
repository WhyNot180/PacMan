import pygame
import random
import Constants as Const
from collections import deque as queue

class Ghost(pygame.sprite.Sprite):

    isScared : bool
    direction : int
    row : int = 1
    column : int = 2

    def __init__(self, colour):
        super(Ghost, self).__init__()
        self.surf = pygame.Surface((25,25))
        self.surf.fill((255,255,255))
        self.rect = self.surf.get_rect(
            center=(
                random.randint(Const.screenWidth + 20, Const.screenWidth + 100),
                random.randint(0, Const.screenHeight),
            )
        )
        self.speed = 5
        self.colour = colour
    # Move the sprite based on speed
    # Remove the sprite when it passes the left edge of the screen
    def update(self, playerRight):
        
        if self.rect.right < playerRight:
            self.direction = 1
        elif self.rect.right > playerRight:
            self.direction = 2
        else:
            self.direction = 0
        
        if self.direction == 1:
            self.rect.move_ip(self.speed, 0)
        elif self.direction == 2:
            self.rect.move_ip(-self.speed, 0)

        # Keep ghost on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > Const.screenWidth:
            self.rect.right = Const.screenWidth
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= Const.screenHeight:
            self.rect.bottom = Const.screenHeight
    
    def scared(self):
        self.isScared = True
    
    def __isVisited(self, visited, row, column):
        # If cell lies out of bounds
        if (row < 0 or column < 0 or row >= len(visited) or column >= len(visited[row])):
            return False
    
        # If cell is already visited
        if (visited[row][column]):
            return False
    
        # Otherwise
        return True
    
    def search(self, playerColumn, playerRow):

        dRow = [-1, 0, 1, 0]
        dColumn = [0, -1, 0, 1]

        visited = [[False for i in range(10)] for i in range(3)]

        grid = [[1,2,3,4,5,6,7,8,9,10],
                [11,12,13,14,15,16,17,18,19,20],
                [21,22,23,24,25,26,27,28,29,30]]

        # Stores indices of the matrix cells
        q = queue()

        prev = queue()
    
        # Mark the starting cell as visited
        # and push it into the queue
        q.append((self.row, self.column))
        visited[self.row][self.column] = True
        reached = False
    
        # Iterate while the queue
        # is not empty
        while ((len(q) > 0) and (not reached)):
            cell = q.popleft()
            x = cell[0]
            y = cell[1]
            print(grid[x][y], end = " ")
            
    
            # Go to the adjacent cells
            for i in range(4):
                adjx = x + dRow[i]
                adjy = y + dColumn[i]
                if (self.__isVisited(visited, adjx, adjy)):
                    q.append((adjx, adjy))
                    visited[adjx][adjy] = True
                    prev.append((adjx, adjy, x, y))
            
            if (x == playerColumn and y == playerRow):
                    reached = True

        if (reached):
            print(prev)
            self.pathTrace(prev)
    #TODO: find direction
    def pathTrace(self, path : queue):
        cell = (0, 0, 0, 0)
        while ((len(path) > 1)):
            cell = path.pop()
            parentX = cell[2]
            parentY = cell[3]

            currentNode = cell

            while (currentNode[0] != parentY and currentNode[1] != parentX):
                currentNode = path.pop()
                print(currentNode)
            
        print(cell, end="L")