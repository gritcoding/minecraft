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

