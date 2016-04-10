import mcpi.minecraft as minecraft
import mcpi.block as block
import time
mc = minecraft.Minecraft.create()

def build_house(width, depth, height):
    pos = mc.player.getTilePos()
    initial_distance = 8
    
    x_range = width
    z_range = depth
    y_range = height
    
    mc.setBlocks(pos.x - x_range,
                 pos.y,
                 pos.z - z_range + initial_distance,
                 pos.x + x_range,
                 pos.y + y_range,
                 pos.z + z_range + initial_distance,
                 block.BRICK_BLOCK.id
                 )
    mc.setBlocks(pos.x - x_range + 1,
                 pos.y,
                 pos.z - z_range + initial_distance + 1,
                 pos.x + x_range - 1,
                 pos.y + y_range - 1,
                 pos.z + z_range + initial_distance - 1,
                 block.AIR.id
                 )

    # leave empty space for an entrance
    entrance_x = pos.x + x_range
    entrance_z = pos.z + initial_distance
    entrance_y = 0 # always on ground floor
    mc.setBlocks(entrance_x, entrance_y,     entrance_z,
                 entrance_x, entrance_y + 1, entrance_z,
                 block.AIR.id)

    # put in a window on the other side
    window_x = pos.x - x_range
    window_z = pos.z + initial_distance
    window_y = 1 # one block above ground floor
    window_height = 1
    window_width = 2
    mc.setBlocks(window_x,  window_y,                 window_z,
                 window_x,  window_y + window_height, window_z + window_width,
                 block.GLASS.id)
    
build_house(4, 4, 3)
