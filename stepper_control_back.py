#!/usr/bin/python37all

import RPi.GPIO as GPIO
import time
from stepper import *
import json
from urllib.request import urlopen

# GPIO setup
GPIO.setmode(GPIO.BCM)
pins = [18,21,22,23,24] # controller inputs: in1, in2, in3, in4, led
for pin in pins:
  GPIO.setup(pin, GPIO.OUT, initial=0)

BYJ = Stepper() #BYJ48 stepper motor

#Open and read from Thingspeak
url = "https://api.thingspeak.com/channels/1558420/feeds.json?api_key=MSQKXFOAG2UMD4NZ&results=1"
response = urlopen(url)
jsonData = json.loads(response.read())
feeds = jsonData["feeds"] # submission data stored in 'feeds' key
curr = feeds[0]['field1'] if feeds != [] else '0' #initialize starting angle as 0
not_zeroed = True # assume motor has not been zeroed

while True:
  try:
    #Read from Thingspeak
    response = urlopen(url)
    jsonData = json.loads(response.read())
    feeds = jsonData["feeds"]
    # Get specific form information
    angle = feeds[0]['field1'] if feeds != [] else '0' #what angle to go to
    button_press = feeds[0]['field2'] if feeds != [] else '6' #which button was pressed
    
    if (button_press == '0' and not_zeroed):
      BYJ.zero()
      not_zeroed = False #indicates that motor has been zeroed
      curr = '0' #sets current angle
    elif (button_press == '1'):
      BYJ.goAngle(int(angle),int(curr))
      not_zeroed = True #motor is no longer zeroed
      curr = angle
  except KeyboardInterrupt:
    GPIO.celanup()