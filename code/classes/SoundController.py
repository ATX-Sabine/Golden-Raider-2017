import subprocess

class SoundController:

  FILES = {
    'MARCH': '../music/march.mp3',
    'RICKROLL': '../music/rickroll.mp3',
    'RESISTANCE': '../music/resistance-march.mp3'
  }

  playing = False

  def start(self, file):
    if self.playing:
      self.stop()
    subprocess.Popen(['mpg123', '-q', file])
    self.playing = True

  def stop(self):
    subprocess.call(['killall', 'mpg123'])
    self.playing = False
