PROJECT TO MAKE BOTS TO PLAY GAMES WITHOUT ANY MANUAL INTERFERENCE.

THERE ARE 2 DIFFERENT CODES:
1) ONE CODE IS OF PIANO TILES WHICH TAKES INSTRUCTIONS FROM MOUSE.
2) SECOND CODE IS OF 2048 WHICH TAKES INSTRUCTIONS FROM KEYBOARD.

LINK FOR GAMES :
1) 2048 : https://2048game.com/
2) Piano tiles : http://www.4j.com/Magic-Piano-Online 
Note: for 2048 coordinates were taken by minimising the window but in piano tiles they were taken with full maximized window in the code.

SCRIPTS :

bot.py : Consists of code for bot of piano tiles 

2048.py : Consists of code for bot of 2048 game

LIBRARIES USED :

IN bot.py :
1) pyautogui : PyAutoGUI lets your Python scripts control the mouse and keyboard to automate interactions with other applications.can be installed by using command pip install pyautogui in command prompt or anaconda prompt

2) time : can be installed by using command pip install time in command prompt or anaconda prompt 
           
3) mss : An ultra fast cross-platform multiple screenshots module in pure python using ctypes.  can be installed by using command pip install mss in command prompt or anaconda prompt 
            
IN 2048.py :
1) pyautogui : PyAutoGUI lets your Python scripts control the mouse and keyboard to automate interactions with other applications.can be installed by using command pip install pyautogui in command prompt or anaconda prompt

2. time : can be installed by using command pip install time in command prompt or anaconda prompt 

3. pil/pillow: Pillow is a Python Imaging Library (PIL), which adds support for opening, manipulating, and saving images.can be installed by using command pip install pillow in command prompt or anaconda prompt

HOW TO GET COORDINATES FOR ANY GAME :

import pyautogui
import time

# get cordinates of grids
def print_mouse_pos():
    while True:
        print(pyautogui.position())
        time.sleep(1)


print_mouse_pos()
Note: this code is also present in the folder.
