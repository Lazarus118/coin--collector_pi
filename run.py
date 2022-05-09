#!/usr/bin/env python
# -*- coding: utf-8 -*-

from time import sleep
import tm1637

# Initialize the display (GND, VCC=3.3V, Example Pins are DIO-20 and CLK21)
Display = tm1637.TM1637(CLK=23, DIO=24, brightness=1.0)

while True:
    digits = [0, 1, 7, 5]
    Display.Show(digits)
    Display.ShowDoublepoint(True)
    sleep(0.2)
    Display.cleanup()
