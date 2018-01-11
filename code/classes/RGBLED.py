import sys
import colorsys
import time

class RGBLED:
  def __init__(self, expander, pins, commonAnode=False):
    self.expander = expander
    self.red = pins[0]
    self.green = pins[1]
    self.blue = pins[2]
    self.commonAnode = commonAnode
    self.expander.enablePWMPins(pins)

  def on(self):
    self.setColor([0xFF, 0xFF, 0xFF])
  def off(self):
    self.setColor([0x00, 0x00, 0x00])
  def setColor(self, color):
    if self.commonAnode:
      color = self.flipValues(color)
    self.expander.setPWMPinValue(self.red, color[0])
    self.expander.setPWMPinValue(self.green, color[1])
    self.expander.setPWMPinValue(self.blue, color[2])
  def flipValues(self, color):
    return [0xFF - color[0], 0xFF - color[1], 0xFF - color[2]]
