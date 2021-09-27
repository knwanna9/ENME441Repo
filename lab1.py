import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
from time import sleep
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)

def call_back(pin):
  pwm = GPIO.PWM(pin, 100) # create PWM object @ 100 Hz 
  try:
    pwm.start(0)                  # initiate PWM at 0% duty cycle
    while 1:
      for dc in range(101):       # loop duty cycle from 0 to 100  
        pwm.ChangeDutyCycle(dc)   # set duty cycle  
        sleep(0.01)               # sleep 10 ms
  except KeyboardInterrupt:       # stop gracefully on ctrl-C
    print('\nExiting')

  pwm.stop()
  GPIO.cleanup()

while True:
  try:
    GPIO.output(4, 0)     # set output to 0V
    sleep(0.5)            # wait 0.5 sec
    GPIO.output(4, 1)     # set output to 3.3V
    sleep(0.5)            # wait 0.5 sec

    GPIO.add_event_detect(5, GPIO.RISING, callback=call_back, bouncetime=100)
    GPIO.add_event_detect(6, GPIO.RISING, callback=call_back, bouncetime=100)
  except KeyboardInterrupt:
    print('\nExiting')
