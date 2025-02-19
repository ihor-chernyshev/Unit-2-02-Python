"""Created by Ihor Chernyshev"""
"""Created on Feb 2025"""
"""This program turns an LED on for one second, repeatedly, but the interval increases each time by 1 more second"""

import time
import board
import digitalio

blink_time = 1
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

while True:
    led.value = True
    time.sleep(blink_time)
    led.value = False
    time.sleep(1)
    blink_time = blink_time + 1
