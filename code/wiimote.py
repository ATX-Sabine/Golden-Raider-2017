import cwiid
import time

print('Press 1 + 2 on the WiiMote Now')
try:
  wii=cwiid.Wiimote()
except RuntimeError:
  print "Error opening wiimote connection"
  quit()
 
print 'Wii Remote connected...\n'