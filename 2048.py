import pyautogui
import time
from PIL import ImageGrab,ImageOps

currentGrid = [0,0,0,0, 
               0,0,0,0,
               0,0,0,0,
               0,0,0,0]

#make four variable with each four directions so it will be easier to mention the directions
UP = 100
LEFT = 101
DOWN = 102
RIGHT = 103

#make scoreGrid which will be helpful in determining score of any grids.
scoreGrid = [50, 30, 15, 5,
             30, -10, 0, 0,
             15,  0,  0, 0,
             5,   0,  0, 0]

# get cordinates of grids 
def print_mouse_pos ():
    while True:
        print(pyautogui.position())
        time.sleep(1)
 print_mouse_pos()


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
  #These are coordinates of grid from bottom right corner so that colour is not white

  #Make a array of all cords so that we can iterate through all cords. 
   cordArray = [cord11,cord12,cord13,cord14,
                 cord21,cord22,cord23,cord24,
                 cord31,cord32,cord33,cord34,
                 cord41,cord42,cord43,cord44]
    
class Values: #Make a class for all of the possible values and named them respectively.
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

    #Make a value array similar to cordArray for easier iteration.
    valueArray= [empty,two,four,eight,sixteen,thirtyTwo,sixtyFour,
                 oneTwentyEight,twoFiftySix,fiveOneTwo,oneZeroTwoFour,twoZeroFourEight]


def getGrid(): #make a function for getting current grid.It will itertate through every grid and match the colour value to find the value at grid.  
    image = ImageGrab.grab()  #takes the screenshot of whole screen.
    grayImage = ImageOps.grayscale(image) #converts image to grayscale.
    for index, cord in enumerate (Cords.cordArray): #It loops through every cord and also keeps an index so that we can update current grid.
        pixel = grayImage.getpixel (cord) 
        pos =Values.valueArray.index(pixel)
        if pos == 0:
            currentGrid[index] = 0
        else:
            currentGrid[index] = pow(2,pos)

#we will need to print some other grids later in the same format so let the function take grid as a parameter.
def printGrid(grid): 
    for i in range (16):
        if i%4 == 0:
            print("[ " + str(grid[i]) + " " + str(grid[i+1]) + " " + str(grid[i+2]) + " " + str(grid[i+3]) + " ]")

def swipeRow(row):
    prev = -1 #previous non-zero element
    i = 0
    temp = [0,0,0,0]

    for element in row:

        if element != 0 : #we skip elements that are zero and useless.
            if prev == -1: #we make prev the first non-zero element and also the first element of temp array.
                prev = element
                temp[i] = element
                i +=1
            elif prev == element:
                temp[i-1] = 2*prev #we make (i-1)th element of the array as 2*prev.
                prev = -1 #make prev=-1 as it can no longer can be added to other element.
            else:
                prev = element
                temp[i] = element
                i += 1

    return temp  #we return the new row temp.

def getNextGrid (grid, move): #make a function getNextGrid with a grid and direction as parameter.

    #make a grid temp,same as the current grid which will store our final grid.
    temp = [0,0,0,0,
            0,0,0,0,
            0,0,0,0,
            0,0,0,0]

    if move == UP:
        for i in range(4) :
            row = []
            for j in range(4):
                row.append(grid[i + 4*j]) #we append elements to the row,splitting the grid vertically.
            row = swipeRow(row)
            for j, val in enumerate(row):
                temp [i + 4*j] = val #get the swiped row and add it to temp.
    
    #done same with other directions.
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

def getScore(grid): #make a function which returns the score of any grid. 
    score = 0
    for i in range (4):
        for j in range (4):
            score += grid[4*i+j]* scoreGrid[4*i+j] #just multiply each element of scoreGrid with grid.
    return score

def getBestMove(grid): #make a function which gets us the best move for any grid.
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


    maxScore = max(scoreUp,scoreDown,scoreLeft,scoreRight) #Gets max of all scores.
    
    #just comparing to get the best move possible.
    if scoreUp == maxScore:
        return  UP
    elif scoreDown == maxScore:
        return DOWN
    elif scoreLeft == maxScore:
        return LEFT
    else:
        return RIGHT

def isMoveValid(grid,move): #we compare next grid with current grid,if they are the same move is not possible 
    if getNextGrid(grid,move) == grid:
        return  False
    else:
        return True

def performMove(move): #Function so that bot can actually move the grid.
    if move == UP:
        pyautogui.keyDown('up')
        print("Up")
        time.sleep(0.05) #adding a delay between keyup and keydown so that browser has time to recognise them.
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

def main(): #make the main function 
    time.sleep(3) #adding delay so that we have time to focus 2048 window.
    while True:
        getGrid()
        performMove(getBestMove(currentGrid))
        time.sleep(0.1)

if __name__ == '__main__':
    main()







