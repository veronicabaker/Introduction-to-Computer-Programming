"""
slashes.py - 6 points
=====

Write a program that asks for a height and width, and prints out a pattern
based on that height and width.  You __MUST__ use nested loops to do this.  
See the pattern below.

Example Output:
width:
> 5
height:
> 5
|///|
|\\\|
|///|
|\\\|
|///|

width:
> 3
height:
> 3
|/|
|\|
|/|

Hints:
* accumulate characters into an empty string variable
* the rails can be implemented by testing which column you're on (1st or last)
* modulo may be useful for alternating slashes
* go to a new row / new line by appending the new line character (\n)
* again, use nested loops to do this
"""

height = int(input("What should the height be? \n>"))
width = int(input("What should the width be?\n>"))
pattern = ""

for rows in range(1, height + 1):
    if rows % 2 == 0:
        slashes = "/"
    elif rows % 2 != 0:
        slashes = "\\"
    for columns in range(1, width + 1):
        if columns == 1:
            pattern += "|"
        elif columns == width:
            pattern += "| \n"
        else:
            pattern += slashes

print(pattern)