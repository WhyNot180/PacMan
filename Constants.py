# Must be multiple of 13 for grid
screenWidth = 455
screenHeight = 576
# Initializes map layout: 0 = empty space, 1 = obstacle
# Refer to docs for map image
layout = [[1 for i in range(13)],
                      [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                      [1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
                      [1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
                      [1, 0, 0, 0, 0, 1, 1, 1, 0, 0 ,0 ,0, 1],
                      [1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
                      [1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
                      [1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1],
                      [1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1],
                      [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                      [1 for i in range(13)]]

gridRatio = screenWidth/len(layout[0])