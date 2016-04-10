import RPi.GPIO as GPIO
import mcpi.minecraft as minecraft
import mcpi.block as block
import time

LED = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)  # setup for output

GPIO.output(LED, True)
time.sleep(1.0)

GPIO.cleanup()  # reset GPIO and disble circuitry
