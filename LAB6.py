import time
import RPi.GPIO as GPIO
from LED8x8 import LED8X8
import multiprocessing
import random

dataPin, latchPin, clockPin = 20, 26, 19
patern = [0b00000000]*8 #start blank
LED= LED8X8(dataPin, latchPin, clockPin,patern)
posx,posy = [random.randint(0,7)]*2 #starting coordinate of bug
LED.pattern_array[posx] = (1<<posy) #light up LED at coordinate using multiprocessing array
while True:
  try:
   LED.pattern_array[posx] = 0b00000000 #reset row so it doesn't stay on
   posx += random.randint(-1,1) 
   posy += random.randint(-1,1)
   posx = 0 if posx < 0 else 7 if posx > 7 else posx #x-position boundary
   posy = 0 if posy < 0 else 7 if posy > 7 else posy #y-position boundary
   LED.pattern_array[posx] = (1<<posy) #lights up LED
   time.sleep(0.1)
  except Exception as e:   # catch everything, just in case
    print(e)               # delete once code is debugged
    LED.p1.terminate()      # terminate the process
    LED.p1.join(2)          # wait up to 2 sec for process termination before ending code


