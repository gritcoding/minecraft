import mcpi.minecraft as minecraft
import mcpi.block as block
import time
mc = minecraft.Minecraft.create()

def build_tunnel(length, direction):
    print("building a tunnel of length: " + str(length) + " direction: " + str(direction))
    pos = mc.player.getTilePos()

    start_x = pos.x
    start_y = pos.y
    start_z = pos.z

    # setup defaults, which will be changed as needed
    end_x = start_x
    end_y = start_y + 1 # tunnel is 2 units in height
    end_z = start_z
    
    if direction == 1:
        end_x = start_x + length
    elif direction == 2:
        end_x = start_x - length
    elif direction == 3:
        end_z = start_z + length
    elif direction == 4:
        end_z = start_z - length

    mc.setBlocks(start_x, start_y, start_z,
                 end_x,   end_y,   end_z,
                 block.AIR.id)

    # now place some torches using a loop
    interval = 3 # place a torch every 3 units
    i = 0

    torch_x = start_x
    torch_y = 1 # this always stays the same, one block above ground
    torch_z = start_z
    while i < length:
        if i % interval == 0:
            # place torch here. the exact location depends on the direction
            
            if direction == 1:
                torch_x = 1 * i + start_x
            if direction == 2:
                torch_x = -1 * i + start_x
            if direction == 3:
                torch_z = 1 * i + start_z
            if direction == 4:
                torch_z = -1 * i + start_z

            print("placing torch: ", torch_x, torch_y, torch_z)
            mc.setBlock(torch_x, torch_y, torch_z, block.TORCH.id, 1)
                        

            
        i += 1
    

    

length = int(raw_input("length of tunnel?"))
direction = int(raw_input("direction?"))
build_tunnel(length, direction)
