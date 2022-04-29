import serial
import time
import struct


# variables
down = [0,0,180,180,0]
up = [180,180,0,0,180]
pin = [3,2,1,5,4]
handTypes = { #finger down is 0, finger up is 1
    'palm':[1,1,1,1,1],
    'fist':[0,0,0,0,0],
    'fuckyou':[0,0,1,0,0],
    'one':[0,1,0,0,0],
    'two':[0,1,1,0,0],
    'three':[0,1,1,1,0],
    'four':[0,1,1,1,1],
    'pee':[0,0,0,0,1],
    'rock':[0,1,0,0,1],
    'wavedown':[1,0,0,0,0]
}



# Set up serial baud rate
usbport = '/dev/tty.usbmodem14101'

ser = serial.Serial(usbport,9600,timeout=1)
# time.sleep is necessary - it takes some time to open serial port
time.sleep(5)

def sethome():
    for i in range(5):
        write(pin[i],up[i])

def write(motor,i):
    ser.write(struct.pack('>BBB',255,motor,i))

def set(list):# list = [0,0,0,1,1] = position of fingers denoted by 0 or 1
    for i in range(len(list)):
        if list[i] == 0:
            write(pin[i],down[i])
        if list[i] == 1:
            write(pin[i],up[i])

def makeHand(type):
    set(handTypes[type])



def printHand():
    for key in handTypes:
        print(key)

# sethome()
x = input()
while x != 'exit':
    makeHand(x.replace('\n','').replace('\r',''))
