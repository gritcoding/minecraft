import mcpi.minecraft as minecraft
import time
mc = minecraft.Minecraft.create()

while True:
    time.sleep(1)
    pos = mc.player.getTilePos()
    print("x: " + str(pos.x) + " y: " + str(pos.y) + " z: " + str(pos.z))
