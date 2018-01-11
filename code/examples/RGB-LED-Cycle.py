import sys
import math
sys.path.append('../classes')
sys.path.append('../SX1509-WiringPi-Python')
from time import sleep

from RGBLED import RGBLED
from SX1509 import SX1509

expander = SX1509(0x3E)
expander.reset(False)
rgbLED = RGBLED(expander, [5, 6, 7, 8, 4], False)
expander.startInternalClock()

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

hue = 0

while True:
  color = hsv2rgb(hue, 1, 1)
  print(color)
  rgbLED.setColor(color)
  hue += 1
  if hue > 360:
    hue = 0
  sleep(.05)
