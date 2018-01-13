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

expander = SX1509(0x3E)
expander.reset(False)

engineLED = RGBLED(expander, [0, 1, 2, 3], False)
engineLEDLeft = RGBLED(expander, [3, 4, 5, 6], False)
engineLEDRight = RGBLED(expander, [6, 7, 8, 9], False)
bridgeLED = RGBLED(expander, [9, 10, 11, 12], False)

wiimote = WiiMote(None)
wiimote.init()

sound = SoundController()

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

def rickroll():
  sound.start(SoundController.FILES['RICKROLL'])

wiimote.on(WiiMote.WIIMOTE_KEYS['ONE'], rickroll)

def engineOff():
  engineLED.setColor([0, 0, 0])
  engineLEDLeft.setColor([0, 0, 0])
  engineLEDRight.setColor([0, 0, 0])
  bridgeLED.setColor([0, 0, 0])
  sound.stop()

wiimote.on(wiimote.WIIMOTE_KEYS['DOWN'], engineOff)

while True:
  hue = hue + 1
  if hue == 360:
    hue = 0

def hsv2rgb(h, s, v):
  h = float(h)
  s = float(s)
  v = float(v)
  h60 = h / 60.0
  h60f = math.floor(h60)
  hi = int(h60f) % 6
  f = h60 - h60f
  p = v * (1 - s)
  q = v * (1 - f * s)
  t = v * (1 - (1 - f) * s)
  r, g, b = 0, 0, 0
  if hi == 0: r, g, b = v, t, p
  elif hi == 1: r, g, b = q, v, p
  elif hi == 2: r, g, b = p, v, t
  elif hi == 3: r, g, b = p, q, v
  elif hi == 4: r, g, b = t, p, v
  elif hi == 5: r, g, b = v, p, q
  r, g, b = int(r * 255), int(g * 255), int(b * 255)
  return r, g, b