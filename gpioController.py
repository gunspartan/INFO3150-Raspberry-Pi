from gpiozero import LED, Button
import time
from signal import pause

class GPIOController:
    def __init__(self):
        self.COUNT = 5
        self.DELAY = 0.5
        self.red = LED(6)
        self.green = LED(19)
        self.denyBtn = Button(22)
        self.allowBtn = Button(17)

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

    def approveManual(self):
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