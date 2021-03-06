import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)

def call_back(pin):
  p = 19 if pin == 5 else 26
  pwm = GPIO.PWM(p, 100)
  pwm.start(0)     # initiate PWM at 0% duty cycle
  for dc in range(101)+range(100,-1,-1):       # loop duty cycle from 0 to 100  
    pwm.ChangeDutyCycle(dc)   # set duty cycle  
    sleep(0.005) 
 


GPIO.add_event_detect(5, GPIO.RISING, callback=call_back, bouncetime=100)
GPIO.add_event_detect(6, GPIO.RISING, callback=call_back, bouncetime=100)

while True:
  try:
    GPIO.output(13, 0)     # set output to 0V
    sleep(0.5)            # wait 0.5 sec
    GPIO.output(13, 1)     # set output to 3.3V
    sleep(0.5)            # wait 0.5 sec
  except KeyboardInterrupt:
    print('\nExiting')
    GPIO.cleanup()
    break
    
  
