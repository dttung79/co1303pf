# draw a square

from turtle import * # import everything from the turtle module
# define a variable to store the size of the square
size = 50
# move forward by size
forward(size)

left(90) # turn left by 90 degrees
forward(size)
#penup() # lift the pen up
left(90)
forward(size)
#pendown() # put the pen down
left(90)
forward(size)
left(90)

exitonclick() # close the window when clicked on it
