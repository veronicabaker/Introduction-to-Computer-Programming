"""
stars.py - 6 points
=====
Use __nested for loops__ to create the pattern below based on a number that is
entered by the user:


Please enter a number to help me create a pattern:
> 10

 ******** 
* ****** *
** **** **
*** ** ***
****  ****
****  ****
*** ** ***
** **** **
* ****** *
 ********  

1. Ask the user for a number, n
2. Use the number to create a pattern similar to the one above
3. The width and height of the pattern should equal n
4. Use nested for loops with range to do this
5. At the end of your program, print out the pattern
6. Hints:
   a.  the new line character is "\n"
   b.  to construct the diagonal line that cuts through the field of stars
       think of the relationship between the inner loop variable and the
       outer loop variable
   c.  use that relationship to determine whether or not to add a space (" "),
       a star ("*") or a new line ("\n") 
   d.  you may have to concatenate strings both in your outer and inner loop
   e.  see the slides on nested loops for some help

Hint... imagine the rows and columns numbered:

 012345
0 **** 
1* ** *
2**  **
3**  **
4* ** *
5 **** 
"""

n = int(input("What should the dimensions of our pattern be?\n>"))
pattern = ""

for height in range(1, n):
    for width in range(1, n):
        if width == height:
            pattern += " "
        elif width == n - height:
            pattern += " "
        else:
            pattern += "*"
    print(pattern)
    pattern = ""