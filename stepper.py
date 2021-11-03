import RPi.GPIO as GPIO
import time
from ADCThing import Joystick 

GPIO.setmode(GPIO.BCM)
photores = Joystick(0x48)

pins = [18,25,22,23,26] # controller inputs: in1, in2, in3, in4
for pin in pins:
  GPIO.setup(pin, GPIO.OUT, initial=0)

# Define the pin sequence for counter-clockwise motion, noting that
# two adjacent phases must be actuated together before stepping to
# a new phase so that the rotor is pulled in the right direction:
sequence = [ [1,0,0,0],[1,1,0,0],[0,1,0,0],[0,1,1,0],
        [0,0,1,0],[0,0,1,1],[0,0,0,1],[1,0,0,1] ]
        
state = 0  # current position in stator sequence
currentAngle = 0
def delay_us(tus): # use microseconds to improve time resolution
  endTime = time.time() + float(tus)/ float(1E6)
  while time.time() < endTime:
    pass

def halfstep(dir):
  # dir = +/- 1 (ccw / cw)
  state += dir
  if state > 7: state = 0
  elif state <0:state = 7
  for pin in range(4):    # 4 pins that need to be energized
    GPIO.output(pins[pin], sequence[state][pin])
  delay_us(1000)

def moveSteps(steps,dir):
  #moves the actuatiun sequence a given number of halfsteps
  for step in steps:
    halfstep(dir)

# Make a full rotation of the output shaft:
def loop(dir): # dir = rotation direction (cw or ccw)
  for i in range(512): # full revolution (8 cycles/rotation * 64 gear ratio)
    for halfstep in range(8): # 8 half-steps per cycle
      for pin in range(4):    # 4 pins that need to be energized
        GPIO.output(pins[pin], dir[halfstep][pin])
      delay_us(1000)

class Stepper:
  global current_angle
  def goAngle(angle,spd):
    del_theta = angle - current_angle
    if del_theta >= 0 and del_theta < 180:
      dir = ccw
    elif del_theta >= 180 and del_theta <= 360:
      dir = cw
    elif del_theta >= -180 and del_theta < 0:
      dir = cw
    else:
      dir = ccw
    if abs(del_theta)> 180:
      del_theta -= 180
    else:
      pass
   
    steps = del_theta*512/360
    for i in range(steps): # full revolution (8 cycles/rotation * 64 gear ratio)
      for halfstep in range(8): # 8 half-steps per cycle
        for pin in range(4):    # 4 pins that need to be energized
        GPIO.output(pins[pin], dir[halfstep][pin])
      delay_us(spd)
    current_angle = angle
  
  def zero():
    global value
    while True:
      for i in range(steps): # full revolution (8 cycles/rotation * 64 gear ratio)
        for halfstep in range(8): # 8 half-steps per cycle
          for pin in range(4):    # 4 pins that need to be energized
          GPIO.output(pins[pin], dir[halfstep][pin])
        delay_us(1000)
      value = photores.read(0)
		  photores.write(value)
      if value > 90:
         break

