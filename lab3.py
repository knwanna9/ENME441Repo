from ADCthing import Joystick
from time import sleep

while True:
  try:
    print('{:d} , {:d}'. format(Joystick.getX,Joystick.getY))
    sleep(0.1)
  except KeyboardInterrupt:
    print('\nExiting')
    GPIO.cleanup()
    break

