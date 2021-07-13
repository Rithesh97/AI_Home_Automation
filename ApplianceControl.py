#VOICE CONTROLLED AUTOMATIC ON/OFF HOME APPLIANCES
import re
import time
import RPi.GPIO as GPIO
from firebase import firebase
time.sleep(5)
firebase = firebase.FirebaseApplication('https://lucy-2fe33.firebaseio.com/', None)
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(29,GPIO.OUT)
GPIO.setup(31,GPIO.OUT)
GPIO.setup(33,GPIO.OUT)
GPIO.setup(35,GPIO.OUT)
while True:
    name = firebase.get('/voicecontrol','voice')
    name=name[1:-1]
    print (name)
    code="Lucy"
    key1="switch"
    key2="on"
    key3="off"
    key4="light"
    key5="fan"
    key6="AC"
    key7="room"
    key8="hall"
    key9="ok"
    key10="main"
    key11="power"
if code in name and key1 in name and key2 in name and key7 in name and key4 in name :
    GPIO.output(29,1)
    time.sleep(1)#room light on
    firebase.patch('/voicecontrol',{'replay':'ok','voice':'"ok"','roomlight':'"switch on room light"'})
elif code in name and key1 in name and key2 in name and key8 in name and key4 in name :
    GPIO.output(35,1)
    time.sleep(1)#hall light on
    firebase.patch('/voicecontrol',{'replay':'ok','voice':'"ok"','halllight':'"switch onhall light"'})
elif code in name and key1 in name and key2 in name and key5 in name :
    GPIO.output(31,1)
    time.sleep(1)#fan on
    firebase.patch('/voicecontrol',{'replay':'ok','voice':'"ok"','fan':'"switch on fan"'})
elif code in name and key1 in name and key2 in name and key6 in name :
    GPIO.output(33,1)
    time.sleep(1)#ac on
    firebase.patch('/voicecontrol',{'replay':'ok','voice':'"ok"','ac':'"switch on AC"'})
elif code in name and key1 in name and key3 in name and key7 in name and key4 in name :
    GPIO.output(29,0)
    time.sleep(1)#room light off
    firebase.patch('/voicecontrol',{'replay':'ok','voice':'"ok"','roomlight':'"switch off room light"'})
elif code in name and key1 in name and key3 in name and key5 in name :
    GPIO.output(31,0)
    time.sleep(1)#fan off
    firebase.patch('/voicecontrol',{'replay':'ok','voice':'"ok"','fan':'"switch off fan"'})
elif code in name and key1 in name and key3 in name and key6 in name :
    GPIO.output(33,0)
    time.sleep(1)#ac off
    firebase.patch('/voicecontrol',{'replay':'ok','voice':'"ok"','ac':'"switch off AC"'})
elif code in name and key3 in name and key10 in name and key11 in name :
    GPIO.output(33,0)
    GPIO.output(29,0)
    GPIO.output(31,0)
    GPIO.output(35,0)
    time.sleep(1)#main power off
    firebase.patch('/voicecontrol',{'replay':'ok','voice':'"ok"','mp':'"switch on main power"','roomlight':'"switch off room light"','fan':'"switch off fan"','ac':'"switch off AC"','halllight':'"switch off hall light"'})
elif code in name and key1 in code and key2 in name and key10 in name and key11 in name :
    time.sleep(1)#main power on
    firebase.patch('/voicecontrol',{'replay':'ok','voice':'"ok"','mp':'"switch on main power"'})
elif code in name and key1 in name and key3 in name and key8 in name and key4 in name :
    GPIO.output(35,0)
    time.sleep(1)#hall light off
    firebase.patch('/voicecontrol',{'replay':'ok','voice':'"ok"','halllight':'"switch off hall light"'})
elif key9 not in name:
    print(name)
    print("invalid command")
    time.sleep(1)
    firebase.patch('/voicecontrol',{'replay':'invalid','voice':'"ok"'})