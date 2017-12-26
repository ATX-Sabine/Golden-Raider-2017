import sys
import sysccolor
import time

class RGBLED:
  def __init__(self, expander, pins):
    self.expander = expander
    self.red = pins[0]
    self.green = pins[1]
    self.blue = pins[2]
  def on(self):
    self.expander.setPWMPinValue(self.red, 0xFF)
    self.expander.setPWMPinValue(self.green, 0xFF)
    self.expander.setPWMPinValue(self.blue, 0xFF)
  def off(self):
    self.expander.setPWMPinValue(self.red, 0x00)
    self.expander.setPWMPinValue(self.green, 0x00)
    self.expander.setPWMPinValue(self.blue, 0x00)
