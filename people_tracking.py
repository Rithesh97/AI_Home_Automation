#COUNTING NUMBER OF PERSONS INSIDE HOME USING IR SENSOR
import time
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(40,GPIO.IN)
GPIO.setup(38,GPIO.IN)
count=0
ir=0
while True:
    if GPIO.input(40)==0:
        while GPIO.input(38)==1:
            ir=0
        count+=1
        time.sleep(0.5)
        print (count)
    if GPIO.input(38)==0:
        while GPIO.input(40)==1:
            ir=0
        count-=1
        time.sleep(0.5)
        print(count)