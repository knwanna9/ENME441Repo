import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.OUT)

pwm = GPIO.PWM(26, 100)
  pwm.start(0)     # initiate PWM at 0% duty cycle
  for dc in range(100,-1,-1):       # loop duty cycle from 0 to 100  
    pwm.ChangeDutyCycle(dc)   # set duty cycle  
    sleep(0.01)