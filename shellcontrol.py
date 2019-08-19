import os
from pynput.keyboard import Key, Controller
import pyautogui
import subprocess
from subprocess import run, PIPE
import multiprocessing
import time


os.system("./add.py")
os.system("./commit.py")
os.system("gnome-terminal -e 'bash -c \"./user.py | git push; exec bash\"'")

