# Minecraft Programming

Resources
=========

* Introduction to the Minecraft Python API: http://www.stuffaboutcode.com/2013/04/minecraft-pi-edition-api-tutorial.html
* API reference: http://www.stuffaboutcode.com/p/minecraft-api-reference.html

Introduction to Python
======================

Hello World
-----------
* Startup Minecraft PI, create new world.
* Startup Python IDLE (2), create new file.
Enter the following code and run using F5

```python
import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()
mc.postToChat("hello minecraft !")
```

![hello world](https://raw.githubusercontent.com/gritcoding/minecraft/master/screenshots/hello_world.png)

Coordinates
-----------
*Objective:* display coordinates as the play is moving around the screen
```python
import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()

pos = mc.player.getTilePos()
print(pos.x)
print(pos.y)
print(pos.y)
```

* Notice that this prints only one time. 
* Move around and notice how your coordinates change.

![coordinates](https://raw.githubusercontent.com/gritcoding/minecraft/master/screenshots/coordinates.png)

* Explain the print function

Coordinates in a loop
---------------------
*Objective:* show continuously updating coordinates
```python
import mcpi.minecraft as minecraft
import time
mc = minecraft.Minecraft.create()

while True:
    time.sleep(1)
    pos = mc.player.getTilePos()
    print("x: " + str(pos.x) + " y: " + str(pos.y) + " z: " + str(pos.z))
```

* Have the player move around, and look at how coordinates are changing
* Explain the while True loop
* Explain sleep
* Explain the X/Y/Z coordinate system. **Note that in videogames including minecraft, Z is depth**
* Explain what strings and numbers are, and why one must convert numbers to string using +

The fence, if conditions
------------------------
*Objective:* introduce if conditions by detecting on what side of a fence one is

* Go to a flat area
* Build a small fence as shown on the screenshot
* Step on the fence, and walk along it, to determine its orientation. It will be either *x* or *z*.
* Once you know what coordinate you built it along, you're ready to write the code
```python
import mcpi.minecraft as minecraft
import time
mc = minecraft.Minecraft.create()

while True:
    time.sleep(1)
    pos = mc.player.getTilePos()
    if pos.x > -119:
        print("north of the fence")
    elif pos.x < -119:
        print("south of the fence")
    else:
        print("on the fence")
```

![fence](https://raw.githubusercontent.com/gritcoding/minecraft/master/screenshots/fence.png)

The cross, two if conditions
----------------------------
*Objective:* introduce embedded if conditions and creative string concatenation

* Enhance your fence to look like a cross, like in the screenshot
* Figure out where the midpoint is. If previously you built around the *z* coordinate, then this time your other coordinate is *x* and vice versa.
* You're ready to write the code.

```python
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
```

* Explain string concatenation again
* Explain greater or equal versus greater

![cross](https://raw.githubusercontent.com/gritcoding/minecraft/master/screenshots/cross.png)

The tower
---------
*Objective:* introduce programmatic placement of blocks

You can stand anywhere for this. After running, you should see a huge tower of stone blocks either in front of you or behind you.

```python
import mcpi.minecraft as minecraft
import mcpi.block as block
import time
mc = minecraft.Minecraft.create()

pos = mc.player.getTilePos()
for a in range(50):
    mc.setBlock(pos.x+3, pos.y+a, pos.z, block.STONE.id)
```

![tower](https://raw.githubusercontent.com/gritcoding/minecraft/master/screenshots/tower.png)

* Explain the *range(50)*.
* Explain the arguments we're passing to setBlock, and the coordinates.
* Ask the student which coordinate should be increasing.

The bulldozer
-------------
*Objective:* work with more embedded loops and relative coordinates.

* This script lets you clear a large area and leave it suitable for building.
* In minecraft, an empty space is a block of type *AIR*

```python
import mcpi.minecraft as minecraft
import mcpi.block as block
import time
mc = minecraft.Minecraft.create()

player_pos = mc.player.getTilePos()
for x in range(-10,10):
    for z in range(-10,10):
        for y in range(0,10):
            mc.setBlock(player_pos.x+x, player_pos.y+y, player_pos.z+z, block.AIR.id)
```

![bulldozer](https://raw.githubusercontent.com/gritcoding/minecraft/master/screenshots/bulldozer.png)

After running this script, you should find that a large area was cleared as in the screenshot.

* Explain relative positions to the player
* Explain the *range(start,stop)* function, possibly using IDLE
* Explain why the *y* loop starts at zero. It's because in minecraft, sea level is zero, and we want to clear an area, not dig down.


Building a cube, faster
-----------------------
*Objective:* introduce a faster API for building a volume

* The 3 embedded loops to build a cube work fine, but they are a bit tedious to type, and they are slow as you might have seen.
* There is a simple and faster way to build them.

```python
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
```

![cube](https://raw.githubusercontent.com/gritcoding/minecraft/master/screenshots/build_cube.png)

* If we didn't add **initial_distance**, the player would be trapped inside a cube of iron ore.
* The cube may appear in front or behind you, or off to the sides. You may add this initial_distance to the **x** or **z** dimensions to suit your needs.

Hollow cube
-----------
*Objective:* build a cube which is empty. Because solid cubes are not very useful.

* The basic technique is that we build a solid Iron Ore cube first, using the technique above, and then we build a smaller one inside, with blocks of type **AIR**.

```python
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
```

![hollow cube](https://raw.githubusercontent.com/gritcoding/minecraft/master/screenshots/hollow_cube.png)

* Once the cube is built, you can break up a few blocks to convince yourself that it is indeed hollow.
* Explain why we have the +1 / -1
* Explain why the y dimension is special. Because we don't need to hollow out the ground floor.
* For fun: 
 * go in and place some torches.
 * place a few windows using the glass block.
 * place some ladders on the outside to allow easy climbing to the roof.
 * put in some furniture, a bed, a stove, a door.


Building a personalized house
-----------------------------
*Objective:* introduce re-usable functions

* The house construction code will be placed inside a function, taking house dimensions as a parameter.

```python
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
```

![house function](https://raw.githubusercontent.com/gritcoding/minecraft/master/screenshots/house_function.png)

* Explain functions, and parameters
* For fun:
 * Build a staircase inside the house, leading up to the roof.
 * Add torches for extra lighting
* Extra credit:
 * Add multiple windows.
 * Add a *carpet* on the floor.
 * Build a swimming pool next to your house.

The Tunnel
----------
*Objective:* introduce loops with interval and modulo

* The following scripts lets you dig a tunnel, lit up with torches every 3 blocks

```python
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
```

![tunnel](https://raw.githubusercontent.com/gritcoding/minecraft/master/screenshots/tunnel.png)

* Explain the direction concept. We need to know which direction to build in, and that will determine which direction to increase by the length of the tunnel.
* Explain the while loop to build the torches.
* Explain modulo as a way of having steps. In this case, we want torches every 3 blocks.

