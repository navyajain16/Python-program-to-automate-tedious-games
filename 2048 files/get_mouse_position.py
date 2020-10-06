import pyautogui
import time

# get cordinates of grids
def print_mouse_pos():
    while True:
        print(pyautogui.position())
        time.sleep(1)


print_mouse_pos()