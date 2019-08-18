from pynput.keyboard import Key, Controller
import pyautogui
import time


keyboard = Controller()

comando = "git push" 
usuario = "christianFlores94"
password = "2718Chfl"

#parte de adding

comando = "git add ." 

for letter in comando:
	keyboard.press(letter)
	keyboard.release(letter)

pyautogui.hotkey('enter')

time.sleep(5)

# parte de commit
comando = "git commit -m " 
commit = "\"hola\" "
comando = comando + commit 


for letter in comando:
	keyboard.press(letter)
	keyboard.release(letter)

pyautogui.hotkey('enter')

time.sleep(5)

# parte de push

comando = "git push" 

for letter in comando:
	keyboard.press(letter)
	keyboard.release(letter)

pyautogui.hotkey('enter')

time.sleep(10)

for letter in usuario:
	keyboard.press(letter)
	keyboard.release(letter)

pyautogui.hotkey('enter')

time.sleep(5)

for letter in password:
	keyboard.press(letter)
	keyboard.release(letter)

pyautogui.hotkey('enter')
