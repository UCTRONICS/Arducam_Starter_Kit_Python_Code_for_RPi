#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

pins = [11,12,13,15,16,18,22,7]
dats = [0x3f,0x06,0x5b,0x4f,0x66,0x6d,0x7d,0x07,0x7f,0x6f,0x77,0x7c,0x39,0x5e,0x79,0x71,0x80]

def setup():
	GPIO.setmode(GPIO.BOARD)
	for pin in pins:
		GPIO.setup(pin, GPIO.OUT)   # Set pin mode as output
		GPIO.output(pin, GPIO.LOW)

def writeOneByte(val):
	GPIO.output(11, val & 0xfe)  
	GPIO.output(12, val & 0xfd)  
	GPIO.output(13, val & 0xfb)  
	GPIO.output(15, val & 0xf7)  
	GPIO.output(16, val & 0xef)  
	GPIO.output(18, val & 0xdf)  
	GPIO.output(22, val & 0xbf)  
	GPIO.output(7,  val & 0x7f) 

def loop():
	while True:
		for dat in dats:
			writeOneByte(dat)
			time.sleep(0.5)

def destroy():
	for pin in pins:
		GPIO.output(pin, GPIO.HIGH)
	GPIO.cleanup()             # Release resource

if __name__ == '__main__':     # Program start from here
	setup()
	try:
		loop()
	except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be executed.
		destroy()
