import mcpi.minecraft as minecraft
import time
mc = minecraft.Minecraft.create()

while True:
    time.sleep(1)
    pos = mc.player.getTilePos()
    if pos.z < -119:
        north_south = "North"
        if pos.x > 43:
            print(north_south + " West")
        else:
            print(north_south + " East")
    elif pos.z > -119:
        north_south = "South"
        if pos.x > 43:
            print(north_south + " West")
        else:
            print(north_south + " East")

    
