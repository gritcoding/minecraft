import RPi.GPIO as GPIO
import mcpi.minecraft as minecraft
import mcpi.block as block
import time

mc = minecraft.Minecraft.create()

BUTTON = 4

# these are the list of pin numbers that we have connected LEDs to
LED_LIST = [6, 22, 17]

# setup button
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)   # setup for input

# setup LEDs
for LED in LED_LIST:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LED, GPIO.OUT)  # setup for output

try:
    # turn on all LEDs with a loop
    for LED in LED_LIST:
        GPIO.output(LED, True)
    
    while GPIO.input(BUTTON):
        time.sleep(0.1)

    print("button pressed")
    # if the code reaches this place, we hae pressed the button

    # do a countdown
    for LED in LED_LIST:
        time.sleep(1)
        GPIO.output(LED, False)

    mc.postToChat('BULLDOZER!')
    pos = mc.player.getTilePos()
    mc.setBlocks(pos.x - 20,
             pos.y,
             pos.z - 20,
             pos.x + 20,
             pos.y + 20,
             pos.z + 20,
             block.AIR.id
             )
    
finally:
    GPIO.cleanup()  # reset GPIO and disable circuitry
