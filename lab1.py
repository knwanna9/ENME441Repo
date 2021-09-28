import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
from time import sleep
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)

def call_back(pin):
 print("Rise and shine")
 
 '''pwm = GPIO.PWM(16, 100) # create PWM object @ 100 Hz 
 # initiate PWM at 0% duty cycle
    while 1:
      for dc in range(101):       # loop duty cycle from 0 to 100  
        pwm.ChangeDutyCycle(dc)   # set duty cycle  
        sleep(0.01)               # sleep 10 ms
  except KeyboardInterrupt:       # stop gracefully on ctrl-C
    print('\nExiting')'''


GPIO.add_event_detect(5, GPIO.RISING, callback=call_back, bouncetime=100)

while True:
  try:
    GPIO.output(13, 0)     # set output to 0V
    sleep(0.5)            # wait 0.5 sec
    GPIO.output(13, 1)     # set output to 3.3V
    sleep(0.5)            # wait 0.5 sec
  except KeyboardInterrupt:
    print('\nExiting')
    break
  finally:
    GPIO.cleanup()
