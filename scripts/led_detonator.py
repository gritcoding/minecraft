import RPi.GPIO as GPIO
import mcpi.minecraft as minecraft
import mcpi.block as block
import time

mc = minecraft.Minecraft.create()

BUTTON = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON, GPIO.IN)   # setup for input

try:
    while GPIO.input(BUTTON):
        time.sleep(0.1)

    mc.postToChat('BOOM!')
    
finally:
    GPIO.cleanup()  # reset GPIO and disable circuitry
