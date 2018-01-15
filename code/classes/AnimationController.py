from threading import Timer
import sys

sys.path.append("../")

from sabines_utils import hsv2rgb

class AnimationController:

  animating = False

  def __init__(self):
    self.leds = []
    self.animationFunctions = []

  def addLED(self, name, LEDObject):
    self.leds[name] = LEDObject

  def startAnimationFunction(self, aniFunction, timeInterval):
    animating = True
    self.animationFunctions = []
    self.animationFunctions.append(aniFunction)
    self.timeInterval = timeInterval
    self.__runAnimationFunction()

  def __runAnimationFunction(self):
    if(self.animating):
      for function in self.animationFunctions:
        function()
      Timer(self.timeInterval, self.__runAnimationFunction).start()

  def stop(self):
    self.timeInterval = 0
    self.animation = False
  
