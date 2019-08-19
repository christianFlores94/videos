import os
from pynput.keyboard import Key, Controller
import pyautogui
import subprocess
from subprocess import run, PIPE
import multiprocessing
import time

os.system("./add.py")
os.system("./commit.py")

keyboard = Controller()

def push():
	os.system("./push.py")
	return
def writeUser():
	os.system("./user.py")

def writePass():
	os.system("./pass.py")
	pyautogui.hotkey('enter')

p1 = multiprocessing.Process(name='p1', target= push)
p2 = multiprocessing.Process(name='p2', target= writeUser)
p3 = multiprocessing.Process(name='p3', target =writePass)
p1.start()
p1.join()
time.sleep(5)
p2.start()
p2.join()
time.sleep(5)
pyautogui.hotkey('enter')