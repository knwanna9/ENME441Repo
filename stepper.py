import RPi.GPIO as GPIO
import time
from ADCthing import PCF8591

GPIO.setmode(GPIO.BCM)
photores = PCF8591(0x48)
pins = [18,21,22,23,24] # controller inputs: in1, in2, in3, in4
for pin in pins:
  GPIO.setup(pin, GPIO.OUT, initial=0)

# Reverse = clockwise; sequence = counterclockwise
reverse = [ [1,0,0,0],[1,1,0,0],[0,1,0,0],[0,1,1,0],
        [0,0,1,0],[0,0,1,1],[0,0,0,1],[1,0,0,1] ]

current = 0 #initializes current angle as 0
sequence = reverse[:]
sequence.reverse()
state = 0  # current position in stator sequence

def delay_us(tus): # use microseconds to improve time resolution
  endTime = time.time() + float(tus)/ float(1E6)
  while time.time() < endTime:
    pass

def halfstep(direction):
  # dir = +/- 1 (ccw / cw)
  state += direction
  if state > 7: state = 0
  elif state <0:state = 7
  for pin in range(4):    # 4 pins that need to be energized
    GPIO.output(pins[pin], sequence[state][pin])
  delay_us(1000)

class Stepper:

  def goAngle(self,angle,current_angle):
    del_theta = int(angle) - int(current_angle)
    # Check relative postion of new angle to old angle
    # del_theta ends up as an angle between 0 and 180, for shortest path
    if del_theta > 0 and del_theta <= 180:
      direction = sequence # go ccw
      del_theta = abs(del_theta) 
    elif del_theta > 180 and del_theta <= 360:
      direction = reverse # go cw
      del_theta =abs(abs(del_theta)-360)
    elif del_theta > -180 and del_theta <= 0:
      direction = reverse # go cw
      del_theta = abs(del_theta)
    else:
      direction = sequence # go ccw
      del_theta =abs(abs(del_theta)-360)

    steps = int(del_theta*512/360) #maps angle to steps
    for i in range(steps): # full revolution (8 cycles/rotation * 64 gear ratio)
      for halfstep in range(8): # 8 half-steps per cycle
        for pin in range(4):    # 4 pins that need to be energized
            GPIO.output(pins[pin], direction[halfstep][pin])
        delay_us(1500)

  def zero(self):
    global value
    GPIO.output(pins[4],1) #turn on LED
    time.sleep(1) 
    while True:
      # continuously actuate motor
      for halfstep in range(8): # 8 half-steps per cycle
        for pin in range(4):    # 4 pins that need to be energized
          GPIO.output(pins[pin], sequence[halfstep][pin])
        delay_us(1500)
      value = photores.read(0) 
      print(value)
      if value > 166: #dependent on lighting
        GPIO.output(pins[4],0) # turn off motor
        break
