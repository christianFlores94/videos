#!/usr/bin/env python3
from pynput.keyboard import Key, Controller
import pyautogui
import datetime
import time

def timeStap():
	return '{:%Y-%b-%d %H:%M:%S}'.format(datetime.datetime.now())

keyboard = Controller()

# parte de commit
comando = "git commit -m " 
fecha = timeStap()
commit = "\"%s\" " % fecha
comando = comando + commit 


for letter in comando:
	keyboard.press(letter)
	keyboard.release(letter)

pyautogui.hotkey('enter')
