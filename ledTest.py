#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

LedPin1 = 21    #BCM pin21
LedPin2 = 12    #BCM pin12

GPIO.setmode(GPIO.BCM)       # Numbers pins by physical location
GPIO.setup(LedPin1, GPIO.OUT)   # Set pin mode as output
GPIO.setup(LedPin2, GPIO.OUT)
GPIO.output(LedPin1, GPIO.HIGH) # Set pin to high(+3.3V) to off the led
GPIO.output(LedPin2, GPIO.HIGH)
try:
	while True:
		print '...led on'
		GPIO.output(LedPin1, GPIO.LOW)  # led on
		GPIO.output(LedPin2, GPIO.LOW)
		time.sleep(0.5)
		print 'led off...'
		GPIO.output(LedPin1, GPIO.HIGH) # led off
		GPIO.output(LedPin2, GPIO.HIGH)
		time.sleep(0.5)
except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the flowing code will be  executed.
	GPIO.output(LedPin1, GPIO.HIGH)     # led off
	GPIO.output(LedPin2, GPIO.HIGH)
	GPIO.cleanup()                     # Release resource

