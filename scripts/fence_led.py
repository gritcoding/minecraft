import RPi.GPIO as GPIO
import mcpi.minecraft as minecraft
import time
mc = minecraft.Minecraft.create()


LED = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)  # setup for output

led_status = False

# you will have to figure out these numbers by walking along the edges of your fence
z_max = 11
z_min = 6
x_max = 61
x_min = 55


while True:
    time.sleep(0.25)
    pos = mc.player.getTilePos()
    inside_fence = False
    if pos.z > z_min and pos.z < z_max:
        if pos.x > x_min and pos.x < x_max:
            inside_fence = True
    if inside_fence != led_status:
        led_status = inside_fence
        GPIO.output(LED, led_status)
        

 
