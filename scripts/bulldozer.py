import mcpi.minecraft as minecraft
import mcpi.block as block
import time
mc = minecraft.Minecraft.create()

player_pos = mc.player.getTilePos()
for x in range(-10,10):
    for z in range(-10,10):
        for y in range(0,10):
            mc.setBlock(player_pos.x+x, player_pos.y+y, player_pos.z+z, block.AIR.id)
