from SoundController import SoundController
from time import sleep

sound = SoundController()

sound.start(SoundController.FILES['MARCH'])

sleep(5)

sound.stop()