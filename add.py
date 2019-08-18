from pynput.keyboard import Key, Controller
import pyautogui

keyboard = Controller()
#parte de adding
comando = "git add ." 

for letter in comando:
	keyboard.press(letter)
	keyboard.release(letter)

pyautogui.hotkey('enter')
