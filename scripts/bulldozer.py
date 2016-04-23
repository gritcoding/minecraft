import mcpi.minecraft as minecraft
import mcpi.block as block
import time
mc = minecraft.Minecraft.create()

def bulldoze(pos_x, pos_z):
    for x in range(-10,10):
        for z in range(-10,10):
            for y in range(0,20):
                mc.setBlock(pos_x + x, 0 + y, pos_z + z, block.AIR.id)

player_pos = mc.player.getTilePos()

bulldoze(player_pos.x + 10, player_pos.y + 10)
