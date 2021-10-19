#!/usr/bin/python3
# This code runs continually in the background to apply
# the stored PWM slider value to the GPIO output
import RPi.GPIO as GPIO
import time
led_pins = [13,19,26]
gpio.setmode(GPIO.BCM)
for i in led_pins:
  GPIO.setup(i,OUT)

pwm_r = GPIO.PWM(13, 100)
pwm_g = GPIO.PWM(19, 100)
pwm_b = GPIO.PWM(26, 100)

pwm_r.start(0)
pwm_g.start(0)
pwm_b.start(0)

pwm.start(0) # start with LED off
while True:
  with open("LAB4.txt", 'r') as f:
    data = json.load(f)
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