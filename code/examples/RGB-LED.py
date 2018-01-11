import sys
sys.path.append('../classes')
sys.path.append('../SX1509-WiringPi-Python')
from time import sleep

from RGBLED import RGBLED
from SX1509 import SX1509

expander = SX1509(0x3E)
expander.reset(False)
rgbLED = RGBLED(expander, [5, 6, 4, 3, 2, 1], False)
expander.startInternalClock()

while True:
  print('red')
  rgbLED.setColor([0xFF, 0x00, 0x00])
  sleep(1)
  print('green')
  rgbLED.setColor([0x00, 0xFF, 0x00])
  sleep(1)
  print('blue')
  rgbLED.setColor([0x00, 0x00, 0xFF])
  sleep(1)
  print('on')
  rgbLED.on()
  sleep(1)
  print('off')
  rgbLED.off()
  sleep(1)
