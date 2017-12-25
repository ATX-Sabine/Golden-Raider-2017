import cwiid
import time
import sys
sys.path.append('./SX1509-WiringPi-Python')
from SX1509 import SX1509

print('Press 1 + 2 on the WiiMote Now')
try:
  wii=cwiid.Wiimote()
except RuntimeError:
  print "Error opening wiimote connection"
  quit()
 
print 'Wii Remote connected...\n'

print 'Wii Remote connected...\n'
print 'Press some buttons!\n'
print 'Press PLUS and MINUS together to disconnect and quit.\n'
 
wii.rpt_mode = cwiid.RPT_BTN

expander = SX1509(0x3E)

expander.startInternalClock()
expander.setDisableInputBuffer(5, True)
expander.setDisableInputBuffer(6, True)
expander.setDisableInputBuffer(7, True)
expander.setPullupResistor(5, False)
expander.setPullupResistor(6, False)
expander.setPullupResistor(7, False)
expander.setPinDirection(5, 'output')
expander.setPinDirection(6, 'output')
expander.setPinDirection(7, 'output')
expander.setDigitalPinValue(5, 0)
expander.setDigitalPinValue(6, 0)
expander.setDigitalPinValue(7, 0)
expander.startInternalClock()
expander.enableLEDDriver(5, True)
expander.enableLEDDriver(6, True)
expander.enableLEDDriver(7, True)
 
while True:

  button_delay = 0.25
 
  buttons = wii.state['buttons']
 
  # If Plus and Minus buttons pressed
  # together then rumble and quit.
  if (buttons - cwiid.BTN_PLUS - cwiid.BTN_MINUS == 0):
    print '\nClosing connection ...'
    wii.rumble = 1
    time.sleep(1)
    wii.rumble = 0
    exit(wii)
 
  # Check if other buttons are pressed by
  # doing a bitwise AND of the buttons number
  # and the predefined constant for that button.
  if (buttons & cwiid.BTN_LEFT):
    print 'Left pressed'
    expander.setPWMPinValue(5, 0xFF)
    expander.setPWMPinValue(6, 0x00)
    expander.setPWMPinValue(7, 0xFF)
    time.sleep(button_delay)
 
  if(buttons & cwiid.BTN_RIGHT):
    expander.setPWMPinValue(5, 0x00)
    expander.setPWMPinValue(6, 0x00)
    expander.setPWMPinValue(7, 0xFF)
    print 'Right pressed'
    time.sleep(button_delay)
 
  if (buttons & cwiid.BTN_UP):
    expander.setPWMPinValue(5, 0xFF)
    expander.setPWMPinValue(6, 0xFF)
    expander.setPWMPinValue(7, 0xFF)
    print 'Up pressed'
    time.sleep(button_delay)
 
  if (buttons & cwiid.BTN_DOWN):
    print 'Down pressed'
    time.sleep(button_delay)
 
  if (buttons & cwiid.BTN_1):
    print 'Button 1 pressed'
    time.sleep(button_delay)
 
  if (buttons & cwiid.BTN_2):
    print 'Button 2 pressed'
    time.sleep(button_delay)
 
  if (buttons & cwiid.BTN_A):
    print 'Button A pressed'
    time.sleep(button_delay)
 
  if (buttons & cwiid.BTN_B):
    print 'Button B pressed'
    time.sleep(button_delay)
 
  if (buttons & cwiid.BTN_HOME):
    print 'Home Button pressed'
    time.sleep(button_delay)
 
  if (buttons & cwiid.BTN_MINUS):
    print 'Minus Button pressed'
    time.sleep(button_delay)
 
  if (buttons & cwiid.BTN_PLUS):
    print 'Plus Button pressed'
    time.sleep(button_delay)