import serial
import time
import struct



class hand:
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


    def __init__(self):
        # Set up serial baud rate
        usbport = '/dev/tty.usbmodem14101'

        self.ser = serial.Serial(usbport,9600,timeout=1)
        # time.sleep is necessary - it takes some time to open serial port
        time.sleep(2)
    
    def sethome(self):
        for i in range(5):
            self.write(self.pin[i],self.up[i])

    def write(self,motor,i):
        self.ser.write(struct.pack('>BBB',255,motor,i))

    def set(self,list):# list = [0,0,0,1,1] = position of fingers denoted by 0 or 1
        for i in range(len(list)):
            if list[i] == 0:
                self.write(self.pin[i],self.down[i])
            if list[i] == 1:
                self.write(self.pin[i],self.up[i])
    
    def makeHand(self,type):
        self.set(self.handTypes[type])
    
    def resetConnection(self):
        self.ser.close()
        # Set up serial baud rate
        usbport = '/dev/tty.usbmodem14101'
        self.ser = serial.Serial(usbport,9600,timeout=1)
        # time.sleep is necessary - it takes some time to open serial port
        time.sleep(2)
    
    def printHand(self):
        for key, value in self.handTypes:
            print(key)
            
a = hand()
x = input()
while x != 'exit':
    a.makeHand(x)