import os
from pynput.keyboard import Key, Controller
import pyautogui
import subprocess
from subprocess import run, PIPE
import multiprocessing
import time
os.system("gnome-terminal -e 'bash -c \"./add.py; exec bash\"'")
#os.system("./add.py")
os.system("gnome-terminal -e 'bash -c \"./commit.py; exec bash\"'")
os.system("gnome-terminal -e 'bash -c \"./user.py | git push; exec bash\"'")
#os.system("./commit.py")
#os.system("./user.py | git push")
