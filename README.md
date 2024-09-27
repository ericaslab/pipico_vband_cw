# Pi Pico vBand CW Interface

This code is for connecting a Morse Code key to a computer for use with vband, or other applications that support the vband interface.  

## How it works
By default vband listens for dits on the left control, and dahs on the right control of a standard keyboard.  This code emulates a HID keyboard and passes along left paddle as a left ctrl, and right paddle as a right ctrl.  The vband app is responsible for handling the keying functions.  

## Requirements

Pi-Pico or Pi-Pico W

Circuit Python 9.x or greater

## Hardware

- GPIO 0 - Connects to tip of 3.5mm socket

- GPIO 1 - Connects to ring of 3.5mm socket

## Credits
Code used here is based on the Adafruit example code for a four button macropad.  
https://learn.adafruit.com/pico-four-key-macropad/code-the-four-keypad