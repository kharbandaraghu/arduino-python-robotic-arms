import serial
import time
import struct

# using library to minotor keyboard
from pynput import keyboard

# Set up serial baud rate
usbport = '/dev/tty.usbmodem14101'

ser = serial.Serial(usbport,9600,timeout=1)
# time.sleep is necessary - it takes some time to open serial port
time.sleep(2)

#  current vals
cm1 = 69
cm2 = 90
cm3 = 90
cm4 = 150

def write(motor,i):
    ser.write(struct.pack('>BBB',255,motor,i))

def home():
    write(1,60)
    write(2,90)
    write(3,90)
    write(4,150)
    global cm1
    global cm2
    global cm3
    global cm4
    cm1 = 60
    cm2 = 90
    cm3 = 90
    cm4 = 150

home()

def on_press(key):
    global cm1
    global cm2
    global cm3
    global cm4
    try:
        # open anc close the claws
        if key.char == 'p':
            cm4-=5
            write(4,cm4)
        if key.char == 'o':
            cm4+=5
            write(4,cm4)

        # rotate
        if key.char == 'a':
            cm3-=5
            write(3,cm3)
        if key.char == 'd':
            cm3+=5
            write(3,cm3)

        # fwd back
        if key.char == 'w':
            cm1-=5
            write(1,cm1)
        if key.char == 's':
            cm1+=5
            write(1,cm1)

        # height
        if key.char == 'k':
            cm2-=5
            write(2,cm2)
        if key.char == 'l':
            cm2+=5
            write(2,cm2)

        if key.char == 'e':
            home()
            exit()

    except AttributeError:
        print('special key {0} pressed'.format(
            key))

def on_release(key):
    print('{0} released'.format(
        key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()