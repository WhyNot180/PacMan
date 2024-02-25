GAMESTART = False
GAMEOVER = False
GAMEINIT = True

# Must be multiple of 13 for grid
screenWidth = 455
screenHeight = 576
# Initializes map layout: 0 = empty space, 1 = obstacle, 2 = intersection (there'sprobably a better way to do this)
# Refer to docs for map image
layout = [[1 for i in range(13)],
        [1, 2, 0, 0, 2, 0, 0, 0, 2, 0, 0, 2, 1],
        [1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
        [1, 0, 1, 1, 2, 0, 0, 0, 2, 1, 1, 0, 1],
        [1, 2, 0, 0, 2, 1, 1, 1, 2, 0 ,0 ,2, 1],
        [1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
        [1, 0, 1, 1, 2, 0, 0, 0, 2, 1, 1, 0, 1],
        [1, 2, 0, 2, 2, 1, 1, 1, 2, 2, 0, 2, 1],
        [1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1],
        [1, 2, 0, 2, 0, 0, 0, 0, 0, 2, 0, 2, 1],
        [1 for i in range(13)]]

gridRatio = screenWidth/len(layout[0])