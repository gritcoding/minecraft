import time
import mcpi.minecraft as minecraft
import mcpi.block as block
import random
mc = minecraft.Minecraft.create()

def buildWalls(x, y, z):
    mc.setBlock(x-1, y, z-1, block.BRICK_BLOCK.id)
    mc.setBlock(x, y, z-1, block.BRICK_BLOCK.id)
    mc.setBlock(x+1, y, z-1, block.BRICK_BLOCK.id)
    mc.setBlock(x+1, y, z, block.BRICK_BLOCK.id)
    mc.setBlock(x+1, y, z+1, block.BRICK_BLOCK.id)
    mc.setBlock(x, y, z+1, block.BRICK_BLOCK.id)
    mc.setBlock(x-1, y, z+1, block.BRICK_BLOCK.id)
    mc.setBlock(x-1, y, z, block.BRICK_BLOCK.id)

while True:
    time.sleep(1)  # check every second
    x, y, z = mc.player.getTilePos()
    if x == 0 and z == 0:  # trap at x=0, z=0, any y
        mc.postToChat("Trapped")
        for i in range(0,5):  # wall is 5 blocks high
            buildWalls(x, y+i, z)
        time.sleep(3)
        mc.player.setPos(x+10, y+10, z+10) # escape after 3 seconds
        mc.postToChat("Freedom!")
        break  


