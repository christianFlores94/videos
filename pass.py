#!/usr/bin/env python3
from pynput.keyboard import Key, Controller
import pyautogui
import time

keyboard = Controller()
password = "2718Chfl"

for letter in password:
	keyboard.press(letter)
	keyboard.release(letter)
	
pyautogui.hotkey('enter')