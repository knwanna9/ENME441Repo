import RPi.GPIO as GPIO
import time

def map( value, fromLow, fromHigh, toLow, toHigh):
  return (toHigh-toLow)*(value-fromLow) / (fromHigh-fromLow)+ toLow
  
class Servo:

  def servoWrite(motor,angle):      # make the servo rotate to specific angle (0-180 degrees) 
      if(angle<-90):
          angle = -90
      elif(angle > 90):
          angle = 90
      motor.ChangeDutyCycle(map(angle,-90,90,2.5,12.5))#map the angle to duty cycle and output it
      time.sleep(0.25)