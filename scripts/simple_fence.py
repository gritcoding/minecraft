import mcpi.minecraft as minecraft
import time
mc = minecraft.Minecraft.create()

while True:
    time.sleep(1)
    pos = mc.player.getTilePos()
    if pos.z > -119:
        print("North of the fence")
    elif pos.z < -119:
        print("South of the fence")
    else:
        print("On the fence")

    
