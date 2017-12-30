import time
import cwiid
from pydispatch import dispatcher

class WiiMote:
  def __init__(self, wiimoteID):
    # Add code to make sure it's the right wiimote horo
  def checkForNunchuck(self):
    # returs True if attached, False otherwise
  def status(self):
    # pretty prints the status of the wiimote/nunchux