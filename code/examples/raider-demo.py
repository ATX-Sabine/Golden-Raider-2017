import time
import sys
import math
sys.path.append('../SX1509-WiringPi-Python')
from SX1509 import SX1509
sys.path.append('../classes')
from WiiMote import WiiMote
from RGBLED import RGBLED
from SoundController import SoundController
sys.path.append('../')
from sabines_utils import hsv2rgb
from threading import Timer

expander = SX1509(0x3E)
expander.reset(False)

engineLED = RGBLED(expander, [0, 1, 2, 3], False)
engineLEDLeft = RGBLED(expander, [3, 4, 5, 6], False)
engineLEDRight = RGBLED(expander, [6, 7, 8, 9], False)
bridgeLED = RGBLED(expander, [9, 10, 11, 12], False)

wiimote = WiiMote(None)
# wiimote.init()

sound = SoundController()

animating = False
hue = 0

def engineRed():
  engineLED.setColor([255, 0, 0])
  engineLEDLeft.setColor([255, 0, 0])
  engineLEDRight.setColor([255, 0, 0])
  engineLEDRight.setColor([255, 0, 0])

wiimote.on(wiimote.WIIMOTE_KEYS['A'], engineRed)

def imperialMarch():
  engineLED.setColor([0, 0, 255])
  engineLEDLeft.setColor([0, 0, 255])
  engineLEDRight.setColor([0, 0, 255])
  bridgeLED.setColor([100, 100, 100])
  sound.start(SoundController.FILES['MARCH'])

wiimote.on(WiiMote.WIIMOTE_KEYS['B'], imperialMarch)

def rickrollColor():
  global animating, hue
  print("rickrollColor() called")
  print(animating)
  if animating:
    color = hsv2rgb(hue, 1, 1)
    print(color)
    engineLED.setColor([color[0], color[1], color[2]])
    hue = hue + 1
    Timer(0.01, rickrollColor).start()

def rickroll():
  global animating
  sound.start(SoundController.FILES['RICKROLL'])
  animating = True
  print("Setting animating to True")
  print(animating)
  Timer(0.01, rickrollColor).start()

wiimote.on(WiiMote.WIIMOTE_KEYS['ONE'], rickroll)

rickroll()

def engineOff():
  global animating
  animating = False
  engineLED.setColor([0, 0, 0])
  engineLEDLeft.setColor([0, 0, 0])
  engineLEDRight.setColor([0, 0, 0])
  bridgeLED.setColor([0, 0, 0])
  sound.stop()

wiimote.on(wiimote.WIIMOTE_KEYS['DOWN'], engineOff)

Timer(5, engineOff).start()

while True:
  hue = hue