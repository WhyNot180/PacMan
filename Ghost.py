import pygame
import random
import Constants as Const
from collections import deque as queue

class Ghost(pygame.sprite.Sprite):

    isScared : bool
    # 1 is right
    # 2 is left
    # 3 is up
    # 4 is down
    direction = 4
    row : int = 3
    column : int = 4

    layout = [[0,0,0,0,0,0,0,0,1],
              [0,1,1,1,0,1,1,0,0],
              [0,1,1,0,0,1,0,1,0],
              [0,0,0,0,0,0,0,0,0],
              [0,1,1,1,1,1,1,1,0]]

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
        
        #self.direction = self.pathFind(self.direction, self.layout)
        
        if self.direction == 1:
            self.rect.move_ip(self.speed, 0)
        elif self.direction == 2:
            self.rect.move_ip(-self.speed, 0)
        elif self.direction == 3:
            self.rect.move_ip(0, -self.speed)
        elif self.direction == 4:
            self.rect.move_ip(0, self.speed)

        # Keep ghost on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > Const.screenWidth:
            self.rect.right = Const.screenWidth
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= Const.screenHeight:
            self.rect.bottom = Const.screenHeight
    
    def pathFind(self, currentDirection, map):
        path = self.search(1, 0, currentDirection, map)
        cell = self.pathTrace(path, 1, 0)
        print(cell)
        if cell[0] > self.row:
            print("hi 4")
            return 4
        elif cell[0] < self.row:
            print("hi 3")
            return 3
        elif cell[1] > self.column:
            print("hi 2")
            return 1
        elif cell[1] < self.column:
            print("hi 1")
            return 2
    
    def __isVisited(self, visited, row, column):
        # If cell lies out of bounds
        if (row < 0 or column < 0 or row >= len(visited) or column >= len(visited[row])):
            return False
    
        # If cell is already visited
        if (visited[row][column]):
            return False
    
        # Otherwise
        return True
    
    def search(self, playerColumn, playerRow, currentDirection, map):

        dRow = [0, 0, 1, -1]
        dColumn = [-1, 1, 0, 0]

        visited = [[False for i in range(len(self.layout[0]))] for i in range(len(self.layout))]

        grid = map

        for i in range(len(visited[0])):
            for j in range(len(visited)):
                if grid[j][i] == 1:
                    visited[j][i] = True
        

        # Stores indices of the matrix cells
        q = queue()

        prev = queue()

        # Mark the starting cell as visited
        # and push it into the queue
        q.append((self.row, self.column))
        visited[self.row][self.column] = True
        visited[self.row + dRow[currentDirection - 1]][self.column + dColumn[currentDirection - 1]] = True
        print(visited)
        reached = False
    
        # Iterate while the queue
        # is not empty
        while ((len(q) > 0) and (not reached)):
            cell = q.popleft()
            x = cell[0]
            y = cell[1]
            
            # Go to the adjacent cells
            for i in range(4):
                adjx = x + dRow[i]
                adjy = y + dColumn[i]
                if (self.__isVisited(visited, adjx, adjy)):
                    q.append((adjx, adjy))
                    visited[adjx][adjy] = True
                    prev.append((adjx, adjy, x, y))
                if (adjx == playerColumn and adjy == playerRow):
                        reached = True
                        break
            

        if (reached):
            return prev
        
    #TODO: find direction
    def pathTrace(self, path : queue, playerY, playerX):
        cell = path.pop()
        while ((len(path) > 1)):
            x = cell[0]
            y = cell[1]
            parentX = cell[2]
            parentY = cell[3]

            while (x != parentX or y != parentY):
                cell = path.pop()
                x = cell[0]
                y = cell[1]
            
        return (cell[0], cell[1])