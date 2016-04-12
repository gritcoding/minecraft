# Minecraft Programming using Python and Raspberry Pi

## Outline

### General Introductions

### Wooden Block Game
- Minecraft coordinate system:
  - x-axis: East (positive), West (negative)
  - z-axis: South (positive), North (negative)
  - y-axis: High (positive), Low (negative)
  - Right-handed coordinates: thumb = x, index = y, middle = z
  


- Instructions: 
  - B (Block) *x,y,z*
  - L (Loop) *i* = start,end
  - F (Function)
- Task:
  - Write instructions to build a structure.
  - Send your instructions (and parent) to another builder.
  - Win a prize if your structure is built successfully.

### Setup Raspberry Pi

### Introduction to Minecraft
  - What is Minecraft?
  - What is Minecraft Pi (features and limitations).
  - Play the game!
  - Keys:
  
    Key | Action 
    --- | ------
    W	| Forward
    A	| Left 
    S	| Backward 
    D	|	Right
    Left-click | Hit
    Right-click | Place block
    Mouse-scroll | Hotbar select
    E	|	Inventory
    Space	|	Jump
    Double Space	|	Fly / Fall
    Esc	| Pause / Game menu
    Tab	| Release mouse cursor

  - Challenges for parents
    - Move to position 0,0,0
    - Learn to fly and swim
    - Build a house with stone, door, windows and wooden roof (+fence around the house)
    - What are the dimensions of your house?

### Video: pair programming

- Introduction to Python: [intro.py](scripts/intro.py)
  - [RefCard](https://dzone.com/refcardz/core-python)
  - Case-sensitive
  - Indentation for blocks
  - Run: F5
  - Break: CTRL+C 
- [Introduction](MINECRAFT_INTRO.md)
  - tower
  - house (+carpets)
- Magic Carpet
- Treasure Hunt
- [Electronics](MINECRAFT_ELECTRONICS.md)
  - Light an LED
    - non-programatically
    - programatically and blink
    - welcome mat, 3 LEDs: eject countdown
  - try : finally : cleanup
  - 7 segment display?
