#Libraries
#from signal import signal, SIGTERM, SIGHUP, pause
from rpi_lcd import LCD
import RPi.GPIO as GPIO
import time
import multiprocessing
import smbus                    #import SMBus module of I2C
import math
from servo import *
import json
from urllib.request import urlopen

GPIO.setwarnings(False)
#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)

#set GPIO Pins
GPIO_TRIGGER = 26
GPIO_ECHO = 19

#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

motorpins = [16,20,21,13] 
for pin in motorpins:
  GPIO.setup(pin, GPIO.OUT, initial=0)
# lArmPin = 16 ,xRotPin = 21, yRotPin = 20, leftMPin = 13

dcMin = 3
dcMax = 12

pwmx = GPIO.PWM(xRotPin, 50) # controls x rotation servo
pwmy = GPIO.PWM(yRotPin, 50) # controls y rotation servo
pwmL = GPIO.PWM(lArmPin, 50) # controls launch arm servo
pwmM = GPIO.PWM(leftMPin, 50) # controls flywheels
pwmx.start(7.5)
pwmy.start(7.5)
pwmL.start(3)
pwmM.start(0)

#some MPU6050 Registers and their Address
PWR_MGMT_1   = 0x6B
SMPLRT_DIV   = 0x19
CONFIG       = 0x1A
GYRO_CONFIG  = 0x1B
INT_ENABLE   = 0x38
ACCEL_XOUT_H = 0x3B
ACCEL_YOUT_H = 0x3D
ACCEL_ZOUT_H = 0x3F
GYRO_XOUT_H  = 0x43
GYRO_YOUT_H  = 0x45
GYRO_ZOUT_H  = 0x47

def MPU_Init():
        #write to sample rate register
        bus.write_byte_data(Device_Address, SMPLRT_DIV, 7)

        #Write to power management register
        bus.write_byte_data(Device_Address, PWR_MGMT_1, 1)
        #Write to Configuration register
        bus.write_byte_data(Device_Address, CONFIG, 0)

        #Write to Gyro configuration register
        bus.write_byte_data(Device_Address, GYRO_CONFIG, 24)

        #Write to interrupt enable register
        bus.write_byte_data(Device_Address, INT_ENABLE, 1)

def read_raw_data(addr):
        #Accelero and Gyro value are 16-bit
        high = bus.read_byte_data(Device_Address, addr)
        low = bus.read_byte_data(Device_Address, addr+1)

        #concatenate higher and lower value
        value = ((high << 8) | low)

        #to get signed value from mpu6050
        if(value > 32768):
                value = value - 65536
        return value


bus = smbus.SMBus(1)    # or bus = smbus.SMBus(0) for older version boards
Device_Address = 0x68   # MPU6050 device address

MPU_Init()

def readAngle(rot):
  while True:
  #Read Gyroscope raw value
    gyro_x=read_raw_data(GYRO_XOUT_H)
    gyro_y=read_raw_data(GYRO_YOUT_H)
    gyro_z=read_raw_data(GYRO_ZOUT_H)
    #Read Accelerometer raw value
    #acc_x=read_raw_data(ACCEL_XOUT_H)
    #acc_y=read_raw_data(ACCEL_YOUT_H)
    #acc_z=read_raw_data(ACCEL_ZOUT_H)
    #Full scale range +/- 250 degree/C as per sensitivity scale factor
    #Ax = acc_x/16384.0
    #Ay = acc_y/16384.0
    #Az = acc_z/16384.0

    Gx = gyro_x/131.0
    Gy = gyro_y/131.0
    Gz = gyro_z/131.0
    #rad1=math.atan2(Ax,math.sqrt((Ay*Ay)+(Az*Az)))
    #rad2=math.atan2(Ay,math.sqrt((Ax*Ax)+(Az*Az)))
    rot[0]=Gz
    rot[1]=-Gy
    time.sleep(1)

#Read distance fromUltrasonic Sensor
def distance(dist):
  while True:

    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)

    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)

    StartTime = time.time()
    StopTime = time.time()

    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()

    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()

    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    dist.value = (TimeElapsed * 34300) / 2



url = "https://api.thingspeak.com/channels/1558420/feeds.json?api_key=MSQKXFOAG2UMD4NZ&results=1"
response = urlopen(url)
jsonData = json.loads(response.read())
feeds = jsonData["feeds"]
hor_angle = feeds[0]['field1'] if feeds != [] else '90' #what angle to go to
ver_angle = feeds[0]['field2'] if feeds != [] else '90' #what angle to go to
button_press = feeds[0]['field3'] if feeds != [] else '0' #which button was pressed
if hor_angle == 'None':
      hor_angle ='90'
if ver_angle == 'None':
      ver_angle ='90'
if button_press == 'None':
      button_press ='0'


#Run ultrasonic code
dist = multiprocessing.Value('f')
us = multiprocessing.Process(target=distance,args=(dist,))
us.daemon = True
us.start()

#Run Gyroscope code
rot = multiprocessing.Array('f',2)
for i in range(2):
  rot[i] *= 180/math.pi

gyro = multiprocessing.Process(target=readAngle,args=(rot,))
gyro.daemon = True
gyro.start()

lcd = LCD()

if bool(button_press) == 0:
  while True:
    if rot[0] < int(hor_angle):
      pwmx.servoWrite(rot[0]+0.001)
    elif rot[0] > int(hor_angle):
      pwmx.servoWrite(rot[0]-0.001)
    else:
      break
  time.sleep(1)
  while True:
    if rot[1] < int(ver_angle):
      pwmx.servoWrite(rot[1]+0.01)
    elif rot[1] > int(ver_angle):
      pwmy.servoWrite(rot[1]-0.001)
    else:
      break
  time.sleep(1)

elif bool(button_press) == 1:
  #Calculate math and such
  pwmL.ChangeDutyCycle(3) #load projectile
  time.sleep(0.5)
  pwmM.ChangeDutyCycle(100) #run flywheels
  time.sleep(2)
  pwmL.ChangeDutyCycle(12) #push projectile into flywheels
  time.sleep(0.5)
  pwmL.ChangeDutyCycle(3) #return to starting position
  pwmM.ChangeDutyCycle(0) #turn off flywheels
else:
  pass
  

try:
  #signal(SIGTERM, safe_exit)
  #signal(SIGHUP, safe_exit)
  while True:
    lcd.text("Dist = %.1f cm" % dist.value, 1)
    lcd.text("Gx=%.2f " % rot[0] + "Gy=%.2f " % rot[1],2)
    #pause()
except KeyboardInterrupt:
  GPIO.cleanup()
  us.terminate()
  gyro.terminate()
finally:
  lcd.clear()