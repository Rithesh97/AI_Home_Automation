#MEASURING TEMPERATURE AND HUMIDITY
import Adafruit_DHT
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN)
value1=0
value2=0
while True:
    value1,value2= Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 23)
    print(value1)
    value1 = 9/5*value1+32
    print(value1)
    time.sleep(0.2)