"""
spirals.py - 5 points
=====
Draw two spirals using your square function from your previous homework...
and two turtles.  The resulting drawing should look like this:

http://foureyes.github.io/csci-ua.0002-spring2015-008/resources/img/spirals.png

Square Function
* Copy and paste your draw square function from your previous homework.
* Make sure it takes two arguments, a turtle object and an int (modify it
  appropriately if it doesn't)

Spirals
* import turtle, create a Screen object, and call mainloop on your Screen
  object at the end of your program (the usual stuff you do when you write a
  turtle program)
* however, instead of just one turtle, create two Turtle objects:
  don = turtle.Turtle()
  leo = turtle.Turtle()
* set the color of one turtle to 'blue', and the other to 'green'
* without drawing, move one of the turtles away from the other (and put the
  pen back down afterwards)
* using a for loop, have each turtle draw 25 squares... 
  * before drawing each square turn the turtle slightly: leo.left(82)
  * you can use any value you want for turning each turtle (but it should be
    the same for each iteration of the loop)
  * call the square function with the proper turtle variable for each object
    * you can hardcode a value for the size of each square
    * an example call may be: draw_square(don, 57))

Hint: you can speed up drawing by calling speed() on each turtle object:

don.speed(0)
leo.speed(0)
"""
import turtle

t = turtle.Turtle()
r = turtle.Turtle()
wn = turtle.Screen()

t.color('blue')
r.color('green')

t.speed(0)
r.speed(0)

t.up()
t.goto(100,100)
t.down()

def draw_square(obj, length):
    for i in range(4):
        obj.forward(length)
        obj.right(90)


for i in range(25):
    draw_square(t, 50)
    t.left(82)
    draw_square(r, 50)
    r.left(46)


wn.mainloop()