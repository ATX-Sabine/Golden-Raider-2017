import time
import cwiid
import timeinterval

class WiiMote:

  WIIMOTE_KEYS = {
    'UP': 'up',
    'DOWN': 'down',
    'LEFT': 'left',
    'RIGHT': 'right',
    'A':'A',
    'B': 'B',
    'PLUS': 'plus',
    'MINUS': 'minus',
    'HOME': 'home',
    'ONE': 'one',
    'TWO': 'two',
    'POWER': 'power',
    'ANY': 'any'
  }

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
      self.WIIMOTE_KEYS['ANY']: [],
      self.WIIMOTE_KEYS['UP']: [],
      self.WIIMOTE_KEYS['LEFT']: [],
      self.WIIMOTE_KEYS['RIGHT']: [],
      self.WIIMOTE_KEYS['DOWN']: [],
      self.WIIMOTE_KEYS['A']: [],
      self.WIIMOTE_KEYS['B']: [],
      self.WIIMOTE_KEYS['PLUS']: [],
      self.WIIMOTE_KEYS['MINUS']: [],
      self.WIIMOTE_KEYS['HOME']: [],
      self.WIIMOTE_KEYS['ONE']: [],
      self.WIIMOTE_KEYS['TWO']: []
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