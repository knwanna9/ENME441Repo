from ADCthing import Joystick
from time import sleep

#Create object of Joystick class
LAB3_stick = Joystick(0x48)
while True:
  try:
    X = LAB3_stick.getX()
    Y = LAB3_stick.getY()
    print('%3d, %3d' % (X,Y)) #format string- right justified
    sleep(0.1) #100 ms
  except KeyboardInterrupt:
    print('\nExiting')
    break

