#!/usr/bin/env python3
from pynput.keyboard import Key, Controller
import pyautogui
import time

keyboard = Controller()

# parte de push
comando = "git push" 

for letter in comando:
	keyboard.press(letter)
	keyboard.release(letter)

pyautogui.hotkey('enter')

time.sleep(5)
