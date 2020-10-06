from impfiles.swipe_row import swipeRow

# make four variable with each four directions so it will be easier to mention the directions
UP = 100
LEFT = 101
DOWN = 102
RIGHT = 103

def getNextGrid(grid, move):  # make a function getNextGrid with a grid and direction as parameter.

    # make a grid temp,same as the current grid which will store our final grid.
    temp = [0, 0, 0, 0,
            0, 0, 0, 0,
            0, 0, 0, 0,
            0, 0, 0, 0]

    if move == UP:
        for i in range(4):
            row = []
            for j in range(4):
                row.append(grid[i + 4 * j])  # we append elements to the row,splitting the grid vertically.
            row = swipeRow(row)
            for j, val in enumerate(row):
                temp[i + 4 * j] = val  # get the swiped row and add it to temp.

    # done same with other directions.
    elif move == LEFT:
        for i in range(4):
            row = []
            for j in range(4):
                row.append(grid[i * 4 + j])
            row = swipeRow(row)
            for j, val in enumerate(row):
                temp[4 * i + j] = val

    elif move == DOWN:
        for i in range(4):
            row = []
            for j in range(4):
                row.append(grid[i + 4 * (3 - j)])
            row = swipeRow(row)
            for j, val in enumerate(row):
                temp[i + 4 * (3 - j)] = val

    elif move == RIGHT:
        for i in range(4):
            row = []
            for j in range(4):
                row.append(grid[4 * i + (3 - j)])
            row = swipeRow(row)
            for j, val in enumerate(row):
                temp[4 * i + (3 - j)] = val

    return temp