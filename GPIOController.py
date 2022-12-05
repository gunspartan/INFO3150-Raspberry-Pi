from gpiozero import LED, Button
import time
from signal import pause
import os

class GPIOController:
    def __init__(self):
        self.COUNT = 5
        self.DELAY = 0.5
        self.red = LED(19)
        self.green = LED(5)
        self.denyBtn = Button(17)
        self.allowBtn = Button(22)
        self.successSound = 'success.mp3'
        self.denySound = 'deny.mp3'

    def greenOff(self):
        self.green.off()
    def redOff(self):
        self.red.off()

    def allowEntryLED(self):
        for i in range(self.COUNT):
            self.green.on()
            time.sleep(self.DELAY)
            self.green.off()
            time.sleep(self.DELAY)

    def denyEntryLED(self):
        for i in range(self.COUNT):
            self.red.on()
            time.sleep(self.DELAY)
            self.red.off()
            time.sleep(self.DELAY)

    def allowManual(self):
       print("waiting for manual approval")
       if self.allowBtn.wait_for_press(5):
            self.allowEntryLED()
            print("button pressed")
       else:
            print("button not pressed")

    def denyManual(self):
       print("waiting for manual denial")
       if self.denyBtn.wait_for_press(5):
            self.denyEntryLED()
            print("button pressed")
       else:
            print("button not pressed")
        
    def playSound(self, file):
        os.system("mpg321 " + file)
        
    def playApprove(self):
        self.playSound(self.successSound)
        
    def playDeny(self):
        self.playSound(self.denySound)
