import mcpi.minecraft as minecraft
import mcpi.block as block
import time
mc = minecraft.Minecraft.create()

pos = mc.player.getTilePos()
initial_distance = 0
x_range = 20
z_range = 20
y_range = 20
mc.setBlocks(pos.x - x_range,
             pos.y,
             pos.z - z_range + initial_distance,
             pos.x + x_range,
             pos.y + y_range,
             pos.z + z_range + initial_distance,
             block.AIR.id
             )
