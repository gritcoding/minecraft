import mcpi.minecraft as minecraft
import mcpi.block as block
import time
mc = minecraft.Minecraft.create()

pos = mc.player.getTilePos()
initial_distance = 8
x_range = 5
z_range = 5
y_range = 3
mc.setBlocks(pos.x - x_range,
             pos.y,
             pos.z - z_range + initial_distance,
             pos.x + x_range,
             pos.y + y_range,
             pos.z + z_range + initial_distance,
             block.IRON_ORE.id
             )
mc.setBlocks(pos.x - x_range + 1,
             pos.y,
             pos.z - z_range + initial_distance + 1,
             pos.x + x_range - 1,
             pos.y + y_range - 1,
             pos.z + z_range + initial_distance - 1,
             block.AIR.id
             )
