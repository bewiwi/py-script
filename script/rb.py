#!/usr/bin/python
import RPi.GPIO as GPIO
from time import sleep
import sys,getopt
gpio=25
statu=-1
try:
        opts,args = getopt.getopt(sys.argv[1:],'hs:i:')
except getopt.GetoptError:
        print "error ARg"
        sys.exit(1)
for opt,arg in opts:
        if opt == '-s':
                statu=arg
        elif opt == '-i':
                gpio=int(arg)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(gpio, GPIO.OUT)
if statu == '1':
        GPIO.output(gpio,True)
elif statu == '0':
        GPIO.output(gpio,False)
else:
        print GPIO.input(gpio)
