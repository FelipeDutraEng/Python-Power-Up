import pyautogui
from time import sleep

sleep(5)

#pyautogui.position -> pega a posição do mouse
print(pyautogui.position())

# pyautogui.scroll positivo -> sobe
# pyautogui.scroll negativo -> desce
pyautogui.scroll(400)