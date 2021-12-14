import RPi.GPIO as GPIO
import time

def map( value, fromLow, fromHigh, toLow, toHigh):
  return (toHigh-toLow)*(value-fromLow) / (fromHigh-fromLow)+ toLow
  
class Servo:
  def __init__(self,pin):
      servoPin = pin
      global p
      GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
      GPIO.setup(servoPin, GPIO.OUT)   # Set servoPin's mode is output
      GPIO.output(servoPin, GPIO.LOW)  # Set servoPin to low
      p = GPIO.PWM(servoPin, 50)     # set Frequecy to 50Hz
      p.start(7.5)

  def servoWrite(angle):      # make the servo rotate to specific angle (0-180 degrees) 
      if(angle<0):
          angle = 0
      elif(angle > 180):
          angle = 180
      p.ChangeDutyCycle(map(angle,0,180,2.5,12.5))#map the angle to duty cycle and output it
      time.sleep(0.25)