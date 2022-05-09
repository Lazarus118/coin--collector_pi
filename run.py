#!/usr/bin/env python
# -*- coding: utf-8 -*-

from time import sleep
import RPi.GPIO as GPIO
import tm1637

# Initialize the display (GND, VCC=3.3V, Example Pins are DIO-20 and CLK21)
Display = tm1637.TM1637(CLK=23, DIO=24, brightness=1.0)

# disable warnings
GPIO.setwarnings(False)


def _display():
    while (True):
        digits = [0, 1, 7, 5]
        Display.Show(digits)
        Display.ShowDoublepoint(True)
        sleep(0.2)


GPIO.setmode(GPIO.BCM)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
counter = 1
try:
    while True:
        GPIO.wait_for_edge(27, GPIO.RISING)
        print "Pulse coming ! (%s)" % counter
        counter += 1
except KeyboardInterrupt:
    GPIO.cleanup()
