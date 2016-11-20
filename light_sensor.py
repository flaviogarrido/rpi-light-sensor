#!/usr/local/bin/python

import RPi.GPIO as GPIO
import time

__author__ = 'Gus (Adapted from Adafruit)'
__license__ = "GPL"

GPIO.setmode(GPIO.BCM)

#define the pin that goes to the circuit
pin_to_circuit = 26
pin_to_led = 27

#setup led
GPIO.setup(pin_to_led, GPIO.OUT)
GPIO.output(pin_to_led, GPIO.LOW)

def rc_time (pin_to_circuit):
    count = 0

    #Output on the pin for 
    GPIO.setup(pin_to_circuit, GPIO.OUT)
    GPIO.output(pin_to_circuit, GPIO.LOW)
    time.sleep(0.1)

    #Change the pin back to input
    GPIO.setup(pin_to_circuit, GPIO.IN)

    #Count until the pin goes high
    while (GPIO.input(pin_to_circuit) == GPIO.LOW):
        count += 1
	if count > 1000000:
		break

    return count

#Catch when script is interupted, cleanup correctly
try:
    # Main loop
    while True:
        value = rc_time(pin_to_circuit)
        print value
        if(value > 500000):
                GPIO.output(pin_to_led, GPIO.HIGH)
        else:
                GPIO.output(pin_to_led, GPIO.LOW)
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()


