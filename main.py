from pynput import keyboard # https://pynput.readthedocs.io/en/latest/index.html

import winsound


def on_press(key): #sends the key on press to print out in the console
    if key == 'a':
         winsound.Beep(440, 500)
    else:
        try:
            #print('alphanumeric key {0} pressed'.format(key.char))
            if "{0}".format(key.char) == "a":
                winsound.Beep(440, 500)
            else:
                print('alphanumeric key {0} pressed'.format(key.char))
        except AttributeError:
            print('special key {0} pressed'.format(key))

def on_release(key): # sends the key on release to the print out in the console
    print('{0} released'.format(key))
    if key == keyboard.Key.esc: # esc key is the exit condition for the loop
        # stop listener 
        return False
    
with keyboard.Listener( # starts the listener
    on_press=on_press,
    on_release=on_release) as listener:
        listener.join()

