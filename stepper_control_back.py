#!/usr/bin/python37all

import RPi.GPIO as GPIO
import time
import stepper

# GPIO setup
step_motor = Stepper()

while True:
  try:
    # Read from text file created in LAB4_cgi.py
    with open("LAB4.txt", 'r') as f:
      data = json.load(f)
    # Change PWM depending on HTML form selections
    if (data['buttons'] == 'Zero Angle'):
      GPIO.output(pins[5], 1)
      step_motor.zero()

    elif (data['buttons'] == 'Submit'):
      step_motor.goAngle(data['angle'],1000)

  except KeyboardInterrupt:
    GPIO.celanup()