from ADCthing import Joystick
from time import sleep

while True:
  try:
    X = Joystick.getX()
    Y = Joystick.getY()
    print('{:d} , {:d}'. format(X,Y))
    sleep(0.1)
  except KeyboardInterrupt:
    print('\nExiting')
    GPIO.cleanup()
    break

