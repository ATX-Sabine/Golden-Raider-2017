import time
import cwiid
from timeinterval import timeinterval

class WiiMote:
  def __init__(self, wiimoteID):
    # Add code to make sure it's the right wiimote horo
    print('Press 1 + 2 on the WiiMote Now')
    try:
      self.device=cwiid.Wiimote()
    except RuntimeError:
      print "Error opening wiimote connection"
      quit()
    
    print 'Wii Remote connected...\n'

    print 'Wii Remote connected...\n'
    print 'Press some buttons!\n'
    print 'Press PLUS and MINUS together to disconnect and quit.\n'
 
    self.device.rpt_mode = cwiid.RPT_BTN

    self.buttonHandlers = {
      'all': [],
      'up': [],
      'left': [],
      'right': [],
      'down': [],
      'A': [],
      'B': [],
      'plus': [],
      'minus': [],
      'home': [],
      'one': [],
      'two': []
    }

  # set interval to check button here


  def checkForNunchuck(self):
    # returs True if attached, False otherwise
    return False

  def on(self, handler):
    return False

  def buttonsPressed(self):
    return []

  # def status(self):
    # pretty prints the status of the wiimote/nunchux