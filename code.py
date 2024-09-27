# Description: This code is a modified version of the original code from Adafruit
# Use a Pi Pico to hook up an Iambic Morse Keyer to a computer as a USB HID Keyboard.
# Supports the vband cw practice website.  https://hamradio.solutions/vband/
# 
#
#
# Original Code License information:
# SPDX-FileCopyrightText: 2021 john park for Adafruit Industries
# SPDX-License-Identifier: MIT
# Pico Four Key USB HID Keypad

import board
from digitalio import DigitalInOut, Pull, Direction
from adafruit_debouncer import Debouncer
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

kpd = Keyboard(usb_hid.devices)

# define buttons
NUM_KEYS = 4
PINS = (
    board.GP0,
    board.GP1,
    board.GP2,
    board.GP3,
)

KEYMAP = (
    ("Left Control", [Keycode.LEFT_CONTROL]),  # GP0
    ("Right Control", [Keycode.RIGHT_CONTROL]),  # GP1
    (",", [Keycode.COMMA]),  # GP2
    (".", [Keycode.PERIOD]),  # GP3
)

keys = []
for pin in PINS:
    dio = DigitalInOut(pin)
    dio.pull = Pull.UP
    keys.append(Debouncer(dio))

# Setup the onboard LED
led = DigitalInOut(board.LED)
led.direction = Direction.OUTPUT

print("\nWelcome to CW keyer HID Keypad")
print("keymap:")
for k in range(NUM_KEYS):
    print("\t", (KEYMAP[k][0]))


while True:
    pressed_keys = []
    for i in range(NUM_KEYS):
        keys[i].update()
        if keys[i].fell:
            led.value = True  # Turn on the LED when a key is pressed
        if keys[i].rose:
            led.value = False  # Turn off the LED when the key is released
        if keys[i].value == False:  # Key is held down
            pressed_keys.extend(KEYMAP[i][1])
    
    if pressed_keys:
        kpd.send(*pressed_keys)