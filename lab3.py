from ADCthing import Joystick
from time import sleep

LAB3_stick = Joystick(0x48)
while True:
  try:
    X = LAB3_stick.getX()
    Y = LAB3_stick.getY()
    print('%d , %d' % (X,Y))
    sleep(0.1)
  except KeyboardInterrupt:
    print('\nExiting')
    break

