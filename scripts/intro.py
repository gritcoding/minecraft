# Welcome! This is a Python program file

import time
import mcpi.minecraft as minecraft
import mcpi.block as block
import random
mc = minecraft.Minecraft.create()

# The lines that start with a hash (#) are comments
# They are for you to read and are ignored by Python

# When you see 'GO!', save and run the file to see the output
# When you see a line starting with # follow the instructions
# Some lines are python code with a # in front
# This means they're commented out - remove the # to uncomment
# Do one challenge at a time, save and run after each one!

# You can comment out exercises you finish to clear the output
# from previous exercises.

# 1. This is the print statement that prints to the Python Shell

print("Hello world")

# GO!

# You can also print to the Minecraft Chat

#mc.postToChat("Hello Minecraft World")

# GO!

# 2. This is a variable

message = "Level Two"

# Add a line below to print this variable

# GO!

# 3. The variable above is called a string
# You can use single or double quotes (but must close them)
# You can ask Python what type a variable is. Try uncommenting the next line:

#print(type(message))

# GO!

# 4. Another type of variable is an integer (a whole number)
a = 123
b = 654
c = a + b

# Try printing the value of c below to see the answer
# GO!

# 5. You can use other operators like subtract (-) and multiply (*)
# Try some below by replacing the word with the correct operator

#print a times b
#print b minus a
#print 12 times 4
#print 103 add 999
#print 100 divide 25

# GO!

# 6. Variables keep their value until you change it

a = 100
#print(a)  # think - should this be 123 or 100?

c = 50
#print(c)  # think - should this be 50 or 777?

d = 10 + a - c
#print(d)  # think - what should this be now?

# GO!

# 7. You can also use '+' to add together two strings

greeting = 'Hi '
name = ''  # enter your name in this string

message = greeting + name
#mc.postToChat(message)

# GO!

# 8. Try adding a number and a string together and you get an error:

#age =  # enter your age here (as a number)

#mc.postToChat(name + ' is ' + age + ' years old')

# GO!

# See the error? You can't mix types like that.
# But see how it tells you which line was the error?
# Now comment out that line so there is no error

# 9. We can convert numbers to strings like this:

#mc.postToChat(name + ' is ' + str(age) + ' years old')

# GO!

# No error this time, I hope?

# Or we could just make sure we enter it as a string:

# age =  # enter your age here, as a string

# mc.postToChat(name + ' is ' + age + ' years old')

# GO!

# No error this time, I hope?

# You can also print the position of your player:

pos = mc.player.getTilePos()

#mc.postToChat(pos.x)
#mc.postToChat(pos.y)
#mc.postToChat(pos.z)

# The player's position would be easier to read on one line.
# Fix the following code:

#mc.postToChat("x=" + x + " y=" + y + " z=" + z)

# GO!

# Hint: you can simplify the code by getting x, y, z in one go!
# Use the command below to replace the code above.

#x, y, z = mc.player.getTilePos()

# GO!

# 10. Another variable type is called a boolean
# This means either True or False

raspberry_pi_is_fun = True
raspberry_pi_is_expensive = False

# We can also compare two variables using == (equal) or != (not equal)

steves_age = 15
#your_age =  # fill in your age

#print(your_age == steves_age)  # this prints either True or False
#print(your_age != steves_age)  # and what does this print?

# GO!

# 11. We can use less than and greater than too -- these are < and >

#steve_is_older = steves_age > your_age

#print(steve_is_older)  # do you expect True or False?

# GO!

# 12. We can ask questions before printing with an if statement

#south = pos.z < 0

#if south:
#    message = "You are in the South"
#else:
#    message = "You are in the North"

#mc.postToChat(message)  # what do you expect to see here?

# GO!

# Try moving from North to South and running the code above

# We can ask many questions using elif (else if) and use 'not'
# to mean the opposite.

#south = pos.z < 0
#north = not south
#west = pos.x operator 0  # fix me using less than
#east = pos.x operator 0  # fix me using greater than (and equal to)

#if north and east:
#    message = "You are in the North East"
#elif north and west:
#    message = "You are in the North West"
#elif south and east:
#    message = "You are in the South East"
#elif south and west:
#    message = "You are in the South West"

#mc.postToChat(message)

# GO!

# 13. You can create your own commands, or functions using def(ine)

def whereAmI():
    mc.postToChat('You are here.')

# Try 'calling' the function:

#whereAmI()

# GO!

# Now move your North-South-East-West code inside the function.
# Remember to indent! (and also to update position inside the loop)

# Can you call the function many times? (Try from the Shell as well)

# 14. How can we keep the program running continuously while we play?

#while True:
#    whereAmI()

# GO!

# CTRL+C to exit ('while True' will run forever!)

# The loop runs too fast! Can we slow it down?

# Try using the time.sleep(seconds) function inside the loop.

# GO!


# 15. Can we make the loop exit on a 'condition'?
#     How about when the player is at position 0, 0, 0 ?

# Hint: keep looping while x, y, x not equal to 0, 0, 0

# GO!

#while condition:
#    whereAmI()

# 16. We can also loop over numbers

# What do you expect the code below to do? What numbers are printed?
# Can you print 

#for a in range(0, 10):
#    print(a)

# GO!

# 17. It's Minecraft! Let's start building

#mc.setBlock(0, 0, 0, block.STONE.id)

# GO!

# It's not very useful building a block far away from you!
# Can you set the block close to your current position?

# GO!

# 18. Loops + Block = Awesome!

# Let's build a wall (or tower)

#for x in range (start, end):  # replace start and end
#    mc.setBlock(x, y, z, block.BRICK_BLOCK.id)  # fix a value for y and z

# GO!

# Now fix x and loop y to make a tower!

# GO!

# 19. Let's experiment with different types of blocks.

# Press CTRL+SPACE after typing 'block.', or see the list here:
# http://www.stuffaboutcode.com/p/minecraft-api-reference.html

# Note: some blocks have special properties, e.g.

#mc.setBlock(0, 0, 0, block.TNT.id, 1) # '1' means active TNT. Hit it!

#for color in range(0,16):
#    mc.setBlock(0, 0, 0, block.WOOL.id, color) # change color
#    time.sleep(0.5)

# GO!

# Challenge: Can you make a wall of changing colors?
# Advanced: Try random colors using random.randint(0, 15)

# GO!

# 20. You can keep many items in a type of variable called a list

blocks = [block.STONE.id, block.COBBLESTONE.id, block.GRAVEL.id,
          block.SANDSTONE.id, block.MOSS_STONE.id]

#for block in blocks:
#    print block  # what do you expect to see?

# GO!

# A wall with each kind of block:

#x = # where do you want to start?
#for block in blocks:
#    mc.setBlock(x, 10, 10, block)  # what do you expect to see?
#    x = x + 1

# GO!

# Let's build a wall using layers of these blocks.

#y = # where do you want to start?
#z = # fix z to somewhere close to you
#for block in blocks:
#    for x in range (start, end):  # replace start and end
#        mc.setBlock(x, y, z, block)  # change y as you go higher

# GO!

### Congratulations! Your done! On to more programming! ###

