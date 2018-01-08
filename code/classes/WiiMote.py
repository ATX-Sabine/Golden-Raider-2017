import time
import cwiid
import timeinterval

class WiiMote:

  WIIMOTE_KEYS = {
    'UP': cwiid.BTN_UP,
    'DOWN': cwiid.BTN_DOWN,
    'LEFT': cwiid.BTN_LEFT,
    'RIGHT': cwiid.BTN_RIGHT,
    'A': cwiid.BTN_A,
    'B': cwiid.BTN_B,
    'PLUS': cwiid.BTN_PLUS,
    'MINUS': cwiid.BTN_MINUS,
    'HOME': cwiid.BTN_HOME,
    'ONE': cwiid.BTN_1,
    'TWO': cwiid.BTN_2,
    'POWER': 10000,
    'ANY': 'any'
  }

  def __init__(self, wiimoteID):
    self.deviceID = wiimoteID

  def init(self):
    # Add code to make sure it's the right wiimote
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

    self.timer = timeinterval.start(250, self.buttonsPressed)
  
  def close(self):
    timer.stop()
    exit(self.device)

  def checkForNunchuck(self):
    # returs True if attached, False otherwise
    return False

  def on(self, handler):
    return False

  def buttonsPressed(self):
    currentButtonState = self.device.state['buttons']
    result = []
    if(currentButtonState & int(self.WIIMOTE_KEYS['UP'])):
      result.append(self.WIIMOTE_KEYS['UP'])
    if(currentButtonState & int(self.WIIMOTE_KEYS['DOWN'])):
      result.append(self.WIIMOTE_KEYS['DOWN'])
    if(currentButtonState & int(self.WIIMOTE_KEYS['LEFT'])):
      result.append(self.WIIMOTE_KEYS['LEFT'])
    if(currentButtonState & int(self.WIIMOTE_KEYS['RIGHT'])):
      result.append(self.WIIMOTE_KEYS['RIGHT'])
    if(currentButtonState & int(self.WIIMOTE_KEYS['B'])):
      result.append(self.WIIMOTE_KEYS['B'])
    if(currentButtonState & int(self.WIIMOTE_KEYS['A'])):
      result.append(self.WIIMOTE_KEYS['A'])
    if(currentButtonState & int(self.WIIMOTE_KEYS['HOME'])):
      result.append(self.WIIMOTE_KEYS['HOME'])
    if(currentButtonState & int(self.WIIMOTE_KEYS['PLUS'])):
      result.append(self.WIIMOTE_KEYS['PLUS'])
    if(currentButtonState & int(self.WIIMOTE_KEYS['MINUS'])):
      result.append(self.WIIMOTE_KEYS['MINUS'])
    if(currentButtonState & int(self.WIIMOTE_KEYS['ONE'])):
      result.append(self.WIIMOTE_KEYS['ONE'])
    if(currentButtonState & int(self.WIIMOTE_KEYS['TWO'])):
      result.append(self.WIIMOTE_KEYS['TWO'])
    if(currentButtonState & int(self.WIIMOTE_KEYS['POWER'])):
      result.append(self.WIIMOTE_KEYS['POWER'])

    if not len(result) == 0:
      result.append(self.WIIMOTE_KEYS['ANY'])

    return result

  # def status(self):
    # pretty prints the status of the wiimote/nunchux