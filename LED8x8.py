from shifter import Shifter
import time
import RPi.GPIO as GPIO
import multiprocessing

class LED8X8:
  pattern_array = multiprocessing.Array('i',8) #shared memory multiprocessing array
  def __init__(self, data, latch, clock, pattern):
      self.shifter = Shifter(data, latch, clock)

      #Fill multiprocess array with values
      for i in range(len(pattern)):
        self.pattern_array[i] = pattern[i]
      p1 = multiprocessing.Process(target=self.display, args =(self.pattern_array,))#Start new process
      p1.daemon = True
      p1.start()

  def display(self,array):
      while True:
        for row in range(0,8):
          self.shifter.shiftByte(~array[row]) # load the row values
          self.shifter.shiftByte(1 << (row)) # select the given row
          self.shifter.ping(self.shifter.latchPin)
