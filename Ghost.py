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
    direction : int 
    dRow = [0, 0, 1, -1]
    dColumn = [-1, 1, 0, 0]
    row : int = 3
    column : int = 6
    speed = 3

    def __init__(self, colour, layout):
        super(Ghost, self).__init__()
        self.surf = pygame.Surface((Const.gridRatio,Const.gridRatio))
        self.colour = colour
        if self.colour == 'red':
            self.surf.fill((255,0,0))
        elif self.colour == 'blue':
            self.surf.fill((0,255,255))
        elif self.colour == 'pink':
            self.surf.fill((255,170,255))
        elif self.colour == 'orange':
            self.surf.fill((255,170,0))
        else:
            self.surf.fill((255,255,255))
        self.rect = self.surf.get_rect(
            topleft=(
                self.column * Const.gridRatio,
                self.row * Const.gridRatio,
            )
        )

        self.direction = random.randint(1,2)

        self.layout = layout

    def update(self, playerX, playerY, playerDirection):
        
        self.row = round(self.rect.y/Const.gridRatio)
        self.column = round(self.rect.x/Const.gridRatio)

        playerRow = round(playerY/Const.gridRatio)
        playerColumn = round(playerX/Const.gridRatio)

        if self.layout[self.row][self.column] == 2:
            self.direction = self.pathFind(self.direction, self.layout, playerColumn, playerRow, playerDirection)
        
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
    
    def pathFind(self, currentDirection, map, playerColumn, playerRow, playerDirection):
        # if self.colour == 'pink':
        #     path = self.search(playerColumn + 2*self.dColumn[playerDirection-1], playerRow + 2*self.dRow[playerDirection-1], currentDirection, map)
        # else:
        path = self.search(playerColumn, playerRow, currentDirection, map)
        if path != None:
            cell = self.pathTrace(path)
        else:
            return currentDirection
        if cell[0] > self.row:
            return 4
        elif cell[0] < self.row:
            return 3
        elif cell[1] < self.column:
            return 2
        elif cell[1] > self.column:
            return 1
    
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
        visited[self.row + self.dRow[currentDirection - 1]][self.column + self.dColumn[currentDirection - 1]] = True
        print(self.colour)
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
                adjx = x + self.dRow[i]
                adjy = y + self.dColumn[i]
                if (self.__isVisited(visited, adjx, adjy)):
                    q.append((adjx, adjy))
                    visited[adjx][adjy] = True
                    prev.append((adjx, adjy, x, y))
                if (adjx == playerColumn and adjy == playerRow):
                        reached = True
                        break
            
        if (reached):
            return prev
        else:
            return None
        
    #TODO: find direction
    def pathTrace(self, path : queue):
        print(path)
        cell = path.pop()
        while ((len(path) > 1)):
            print(cell)
            x = cell[0]
            y = cell[1]
            parentX = cell[2]
            parentY = cell[3]

            if parentX == self.row and parentY == self.column:
                break

            while (x != parentX or y != parentY):
                print(cell)
                cell = path.pop()
                x = cell[0]
                y = cell[1]
            
        return (cell[0], cell[1])