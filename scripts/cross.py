import mcpi.minecraft as minecraft
import time
mc = minecraft.Minecraft.create()

while True:
    time.sleep(1)
    pos = mc.player.getTilePos()
    if pos.x > -119:
        north_south = "north"
        if pos.z > 43:
            print(north_south + "/west")
        else:
            print(north_south + "/east")
    elif pos.x < -119:
        north_south = "south"
        if pos.z > 43:
            print(north_south + "/west")
        else:
            print(north_south + "/east")

    
