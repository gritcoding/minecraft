# Minecraft Programming

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
* Explain sleep
* Explain the X/Y/Z coordinate system. *Note that in videogames including minecraft, Z is depth*
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

* Explain why we have the +1 / -1
* Explain why the y dimension is special. Because we don't need to hollow out the ground floor.
