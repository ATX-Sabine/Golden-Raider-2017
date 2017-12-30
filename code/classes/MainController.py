from pydispatch import dispatcher

from SoundController import SoundController
from WiiMote import WiiMote

class MainController:
  def __init__(self, wiimoteID):
    self.wiimoteID = wiimoteID