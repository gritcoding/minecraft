import RPi.GPIO as GPIO
import mcpi.minecraft as minecraft
import mcpi.block as block
import time

LED = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)

def flash(t):
    GPIO.output(LED, True)  # LED on
    time.sleep(t)
    GPIO.output(LED, False) # LED off
    time.sleep(t)

try:
    while True:
        flash(seconds)  # how many seconds to flash?
finally:
    GPIO.cleanup()


