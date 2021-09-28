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
 


GPIO.add_event_detect(5, GPIO.RISING, callback=call_back, bouncetime=100)

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
    
  
