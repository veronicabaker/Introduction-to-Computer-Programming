"""
squares.py - 5 points
=====

Draw 5 squares, each with a different size by using the turtle module and 
creating a function.  

* write all of the setup code to get turtle working
* define a function to draw a square; it should take *two arguments*
	* a turtle (you can name this parameter whatever you like)
	* the length of a side of the square (you can name this parameter whatever you like)
* within the body of the function, use a for loop to draw your square
	* use forward
	* use right
* call your function 5 times to draw 5 squares in a row
	* the squares should have a length of 10, 20, 30, 40, and 50 pixels
	* each square should be 5 pixels away from the other square

Example:
http://foureyes.github.io/csci-ua.0002-spring2015-008/resources/img/squares.png
"""
import turtle

t = turtle.Turtle()
wn = turtle.Screen()

def draw_square(obj, length):
    for i in range(4):
        obj.forward(length)
        obj.right(90)
    obj.up()
    obj.forward(length + 5)
    obj.down()

draw_square(t, 10)
draw_square(t, 20)
draw_square(t, 30)
draw_square(t, 40)
draw_square(t, 50)

wn.mainloop()