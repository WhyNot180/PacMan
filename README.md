# A Pac Man Replica

Table of Contents:
- [Why Make This?](#why-make-this)
- [Installation](#installation)
- [Implemented Features](#implemented-features)
- [How The Code Works](#how-the-code-works)
    - [Map](#map)
    - [Player](#player)
    - [Ghosts](#ghosts)
    - [Collectables](#collectables)
    - [Levels](#levels)

## Why Make This?

This replica has been created in order to demonstrate Object-Oriented-Programming. Additionally, this was created partly as a challenge of our programming skills.

## Installation

Currently, the game is still in development and requires [python](https://www.python.org/downloads/) installed in order to run.

Additionally, pygame is also required. In order to install pygame you need to go to the terminal and type the following **after python is installed**:

Windows:
```
pip pygame
```

MacOS:
```
pip3 pygame
```

Once both are installed you can run the game by typing in the terminal in the folder where the game is located:
```
python Main.py
```

## Implemented Features

- [x] Player
    - [x] Collectable collection
    - [x] Can be killed by enemies
- [x] Enemies
    - [x] Enemy tracking
    - [ ] Enemy personalities
- [x] Collectables
    - [x] Pellets
    - [ ] Power pellets
    - [ ] Fruits
- [x] Map
    - [ ] Warp tunnels
    - [ ] Ghost cage
    - [ ] Switch between multiple map layouts
    - [ ] Map builder
- [ ] Levels
- [ ] Appropriate sprites
- [x] Gameover

## How The Code Works

### Map

The map is stored as a 2-D array, where 0 is an empty space, 1 is an obstacle (such as a wall), and 2 is an intersection.
The original design can be seen below:

![](Docs/Images/Original%20Map.jpg)

The map uses a grid coordinate system in order to place obstacles and help with enemy path-finding. To convert between pixel coordinates and grid coordinates, the pixel coordinates are divided by the grid ratio (tile width) and rounded.

```python
row = round(y/gridRatio)
column = round(x/gridRatio)
```

Using these coordinates as well as the 2-D array, we can use a breadth-first-search to allow the enemies to path-find toward a selected point, as well as automatically place obstacles and pellets in selected places (1 for obstacle, 0 and 2 for pellets).

### Player

The player is currently represented by controllable orange square. The player moves in a set direction until it hits a wall or the arrow keys are pressed, changing its direction. The player is also able to collide with enemies, restarting the game, and pellets, earning points.

### Ghosts

### Collectables
