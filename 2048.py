import pyautogui
import time
from PIL import ImageGrab,ImageOps

currentGrid = [0,0,0,0,
               0,0,0,0,
               0,0,0,0,
               0,0,0,0]

UP = 100
LEFT = 101
DOWN = 102
RIGHT = 103

scoreGrid = [50, 30, 15, 5,
             30, -10, 0, 0,
             15,  0,  0, 0,
             5,   0,  0, 0]

class Cords:
    cord11 = (200,345)
    cord12 = (313,345)
    cord13 = (420,345)
    cord14 = (530,345)
    cord21 = (200,455)
    cord22 = (313,455)
    cord23 = (420,455)
    cord24 = (530,455)
    cord31 = (200,562)
    cord32 = (313,562)
    cord33 = (420,562)
    cord34 = (530,562)
    cord41 = (200,672)
    cord42 = (313,672)
    cord43 = (420,672)
    cord44 = (530,672)

    cordArray = [cord11,cord12,cord13,cord14,
                 cord21,cord22,cord23,cord24,
                 cord31,cord32,cord33,cord34,
                 cord41,cord42,cord43,cord44]

class Values:
    empty = 195
    two = 230
    four = 225
    eight = 190
    sixteen = 172
    thirtyTwo = 157
    sixtyFour = 135
    oneTwentyEight = 205
    twoFiftySix = 202
    fiveOneTwo = 197
    oneZeroTwoFour = 193
    twoZeroFourEight = 189

    valueArray= [empty,two,four,eight,sixteen,thirtyTwo,sixtyFour,
                 oneTwentyEight,twoFiftySix,fiveOneTwo,oneZeroTwoFour,twoZeroFourEight]


def getGrid():
    image = ImageGrab.grab()
    grayImage = ImageOps.grayscale(image)
    for index, cord in enumerate (Cords.cordArray):
        pixel = grayImage.getpixel (cord)
        pos =Values.valueArray.index(pixel)
        if pos == 0:
            currentGrid[index] = 0
        else:
            currentGrid[index] = pow(2,pos)

def printGrid(grid):
    for i in range (16):
        if i%4 == 0:
            print("[ " + str(grid[i]) + " " + str(grid[i+1]) + " " + str(grid[i+2]) + " " + str(grid[i+3]) + " ]")

def swipeRow(row):
    prev = -1 #previous non-zero element
    i = 0
    temp = [0,0,0,0]

    for element in row:

        if element != 0 :
            if prev == -1:
                prev = element
                temp[i] = element
                i +=1
            elif prev == element:
                temp[i-1] = 2*prev
                prev = -1
            else:
                prev = element
                temp[i] = element
                i += 1

    return temp

def getNextGrid (grid, move):

    temp = [0,0,0,0,
            0,0,0,0,
            0,0,0,0,
            0,0,0,0]

    if move == UP:
        for i in range(4) :
            row = []
            for j in range(4):
                row.append(grid[i + 4*j])
            row = swipeRow(row)
            for j, val in enumerate(row):
                temp [i + 4*j] = val

    elif move == LEFT:
        for i in range(4) :
            row = []
            for j in range(4):
                row.append(grid[i*4 + j])
            row = swipeRow(row)
            for j, val in enumerate(row):
                temp [4*i + j] = val

    elif move == DOWN:
        for i in range(4) :
            row = []
            for j in range(4):
                row.append(grid[i + 4*(3-j)])
            row = swipeRow(row)
            for j, val in enumerate(row):
                temp [i + 4*(3-j)] = val

    elif move == RIGHT:
        for i in range(4) :
            row = []
            for j in range(4):
                row.append(grid[4*i + (3-j)])
            row = swipeRow(row)
            for j, val in enumerate(row):
                temp [4*i + (3-j)] = val




    return temp

def getScore(grid):
    score = 0
    for i in range (4):
        for j in range (4):
            score += grid[4*i+j]* scoreGrid[4*i+j]
    return score

def getBestMove(grid):
    scoreUp =getScore(getNextGrid(grid,UP))
    scoreDown = getScore(getNextGrid(grid, DOWN))
    scoreLeft = getScore(getNextGrid(grid, LEFT))
    scoreRight = getScore(getNextGrid(grid, RIGHT))

    if not isMoveValid(grid, UP):
        scoreUp = 0
    if not isMoveValid(grid, DOWN):
        scoreDown = 0
    if not isMoveValid(grid, LEFT):
        scoreLeft = 0
    if not isMoveValid(grid, RIGHT):
        scoreRight = 0


    maxScore = max(scoreUp,scoreDown,scoreLeft,scoreRight)

    if scoreUp == maxScore:
        return  UP
    elif scoreDown == maxScore:
        return DOWN
    elif scoreLeft == maxScore:
        return LEFT
    else:
        return RIGHT

def isMoveValid(grid,move):
    if getNextGrid(grid,move) == grid:
        return  False
    else:
        return True

def performMove(move):
    if move == UP:
        pyautogui.keyDown('up')
        print("Up")
        time.sleep(0.05)
        pyautogui.keyUp('up')
    elif move == DOWN:
        pyautogui.keyDown('down')
        print("Down")
        time.sleep(0.05)
        pyautogui.keyUp('down')
    elif move == LEFT:
        pyautogui.keyDown('left')
        print("Left")
        time.sleep(0.05)
        pyautogui.keyUp('left')
    else :
        pyautogui.keyDown('right')
        print("Right")
        time.sleep(0.05)
        pyautogui.keyUp('right')

def main():
    time.sleep(3)
    while True:
        getGrid()
        performMove(getBestMove(currentGrid))
        time.sleep(0.1)

if __name__ == '__main__':
    main()





#2 230
#blank 195
#32 157
#4 225
#8 190
#512 197
#128 205
#16 172
#64 135
#256 202
#1024 193
#2048 189


