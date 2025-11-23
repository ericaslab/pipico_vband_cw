import board
import digitalio
import storage
import time

button_pin = board.GP0

button = digitalio.DigitalInOut(button_pin)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP 

# Give it a moment to stabilize and check the button state
time.sleep(0.1)

# If the button is NOT pressed (HIGH with pull-up), disable the drive
# Button is pressed when value is False (connected to ground)
if button.value:
    storage.disable_usb_drive()