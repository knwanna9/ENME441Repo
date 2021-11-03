#!/usr/bin/python37all

import RPi.GPIO as GPIO
import time
# GPIO setup
led_pins = [13,19,26]
GPIO.setmode(GPIO.BCM)
for i in led_pins:
  GPIO.setup(i,GPIO.OUT)

pwm_r = GPIO.PWM(led_pins[0], 100)
pwm_g = GPIO.PWM(led_pins[1], 100)
pwm_b = GPIO.PWM(led_pins[2], 100)

pwm_r.start(0)
pwm_g.start(0)
pwm_b.start(0)

while True:
  try:
    # Read from text file created in LAB4_cgi.py
    with open("LAB4.txt", 'r') as f:
      data = json.load(f)
    # Change PWM depending on HTML form selections
    if (data['led'] == 'red'):
        brightness = int(data['slider1'])
        pwm_r.ChangeDutyCycle(brightness)
    elif (data['led'] == 'green'):
        brightness = int(data['slider1'])
        pwm_g.ChangeDutyCycle(brightness)
    elif (data['led'] == 'blue'):
        brightness = int(data['slider1'])
        pwm_b.ChangeDutyCycle(brightness) 
    time.sleep(0.1)
  except KeyboardInterrupt:
    GPIO.celanup()