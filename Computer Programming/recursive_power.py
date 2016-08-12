"""
recursive_power.py (5 points)
=====

1.  Create a function called recursive_power:

    * takes two arguments, a number and a power
    * it returns the number raised to the power
    * use recursion to calculate the power
        * define recursive_power by calling itself
        * have a base case, where the function does not call itself
        * do not use the ** operator
        * do not use the ^ operator (this isn't what you think!)
        * do not use the pow function
        * hint: read sections 12.1 and 12.2 in Starting Out With Python

2.  Create at least two assertions to test your function.  These assertions 
    should test the following conditions:

    * if the power is 0, always return 1
    * if the power is over zero, return the number raised to that power

3.  Lastly, call your function once at the end of your program:

	* create a variable and assign the result of... 
	* calling your function with the arguments 2 and 8
	* print out the result

IPO
-----
input: two numbers - the base and the exponent or power
processing: raise the base to the power specified
output: the result of raising the base to the power

Example Usage
-----
result = recursive_power(3, 4)
print(result)
# prints out  81
"""

def recursive_power(base, exponent):
    if exponent == 0:
        return 1
    return base * recursive_power(base, exponent - 1)

assert 81 == recursive_power(3, 4), "3^4 = 81"
assert 1 == recursive_power(3, 0), "n^0 = 1"

result = recursive_power(2, 8)

print(result)