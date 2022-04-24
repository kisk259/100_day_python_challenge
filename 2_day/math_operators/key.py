import random
from pynput.keyboard import Key, Controller
import time

keyboard = Controller()
keys = 'asdw'

while 1:
    time.sleep(10)
    x = random.choice(keys)
    keyboard.press(x)
    print(x)
    time.sleep(2)
    keyboard.release(x)