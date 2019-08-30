#!/usr/bin/env python3
# Author:Zoli
import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
pin = 18 #Pin number

GPIO.setup(pin, GPIO.OUT)
def setPin(mode):
    GPIO.output(pin, mode)
    return()
def pinON():
    setPin(True)
    return()
def pinOFF():
    setPin(False)
    return()
try:
        pinON()
        sleep(3) #Duration (second)
        pinOFF()

except KeyboardInterrupt: # trap a CTRL+C keyboard interrupt
    GPIO.cleanup()
