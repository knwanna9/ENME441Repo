# LEDdisplay class
import time
from shifter import Shifter    # extend by composition
class LEDdisplay():
  'Class for controlling a 7-segment LED display'
  numbers = [ 
    0b11111100, # 0
    0b01100000, # 1
    0b11011010, # 2
    0b11110010, # 3
    0b01100110, # 4
    0b10110110, # 5
    0b10111110, # 6
    0b11100000, # 7
    0b11111110, # 8
    0b11100110] # 9
  def __init__(self, data, latch, clock):
    self.shifter = Shifter(data, latch, clock)
  def setNumber(self, num):  # display a given number
    row = 4 # change this value to pick which row the pattern appears on
    self.shifter.shiftByte(LEDdisplay.numbers[num]) # load the row values
    self.shifter.shiftByte(1 << (row-1)) # select the given row