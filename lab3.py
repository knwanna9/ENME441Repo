from ADCthing import Joystick
from time import sleep

whille True:
  try:
    print('{:d} , {:d}'. format(Joystick.getX,Joystick.getY))
    sleep(0.1)
  except KeyboardInterrupt:
    print('\nExiting')
    GPIO.cleanup()
    break

