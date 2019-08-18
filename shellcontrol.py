from pynput.keyboard import Key, Controller

keyboard = Controller()

comando = "git add ."

for letter in comando:
	keyboard.press(letter)
	keyboard.release(letter)
	