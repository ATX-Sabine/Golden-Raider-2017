import sys
import syscolor
import time

class RGBLED:
  def __init__(self, expander, pins, commonAnode=False):
    self.expander = expander
    self.red = pins[0]
    self.green = pins[1]
    self.blue = pins[2]
    self.commonAnode = commonAnode
  def on(self):
    value = self.commonAnode ? 0x00 : 0xFF
    self.setColor((value, value, value))
  def off(self):
    value = self.commonAnode ? 0xFF : 0x00
    self.setColor((value, value, value))
  def setColor(color):
    if self.commonAnode:
      color = flipValues(color)
    self.expander.setPWMPinValue(self.red, color[0])
    self.expander.setPWMPinValue(self.green, color[1])
    self.expander.setPWMPinValue(self.blue, color[2])
  def flipValues(color):
    color[0] = 0xFF - color[0]
    color[1] = 0xFF - color[1]
    color[2] = 0xFF - color[2]
    return color
