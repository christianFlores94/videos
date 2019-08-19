#!/usr/bin/env python3
from pynput.keyboard import Key, Controller
import pyautogui

keyboard = Controller()

# parte de commit
comando = "git commit -m " 
commit = "\"nuevo\" "
comando = comando + commit 


for letter in comando:
	keyboard.press(letter)
	keyboard.release(letter)

pyautogui.hotkey('enter')
