import sys
sys.path.append('../classes')
sys.path.append('../SX1509-WiringPi-Python')
from time import sleep

from RGBLED import RGBLED
from SX1509 import SX1509

expander = SX1509(0x3E)
commonAnodeRGBLED = RGBLED(expander, [5, 6, 7], True)
expander.startInternalClock()

while True:
  print('on')
  commonAnodeRGBLED.on()
  sleep(1)
  print('off')
  commonAnodeRGBLED.off()
  sleep(1)
