import time
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(40,GPIO.IN)
GPIO.setup(38,GPIO.OUT)
value=0
while True:
    value=GPIO.input(40)
    print(value)
    GPIO.output(38,value)
    time.sleep(0.5)