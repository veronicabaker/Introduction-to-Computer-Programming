"""
lots_of_stars.py - 5 points
=====
Draw a night sky using turtle and a function to draw a star

* write all of the setup code to get turtle working
* define a function to draw a star
* see the image in #9 of chapter 4 in thinksci:
	* http://openbookproject.net/thinkcs/python/english3e/functions.html#exercises
	* (don't hardcode the length, though!)
* it should take *two arguments*
	* a turtle (you can name this parameter whatever you like)
	* the length of a side of the 5 pointed star (you can name this parameter 
      whatever you like)
* call your function at least 20 times to draw a star in a random location 
	* the background should be black
	* the stars should be yellow
	* the stars should have a random length between 5 and 60
	* hint: use the Turtle object's goto method in conjunction with pen up 
      and pen down

Example:
http://foureyes.github.io/csci-ua.0002-spring2015-008/resources/img/lots_of_stars.png
"""

import random
import turtle

t = turtle.Turtle()
wn = turtle.Screen()

wn.bgcolor('black')
t.color('yellow')

def stars(obj, length):
    obj.forward(length)
    obj.right(144)

for i in range(20):
    length = random.randint(5, 60)
    for star in range(5):
        stars(t, length)
    t.up()
    t.goto(random.randint(-250, 250), random.randint(-250, 250))
    t.down()

wn.mainloop()