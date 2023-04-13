import pyautogui
from pyautogui import *


img = locateOnScreen('1.png',confidence = 0.9)

img_center = center(img)

print(img_center)

pyautogui.moveTo(img_center)

pyautogui.leftClick()