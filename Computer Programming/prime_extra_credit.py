"""
prime_extra_credit.py (EXTRA CREDIT - 2 points)
====
Improve the brute force algorithm that you used in the previous assignment.
For example, you don't have to test all of the numbers between 1 and the
original number.  Some things to try:

* if a number is even, it can't be prime (it will always also be divisible
  by 2!)
* stopping at a certain factor - such as the square root

Test your new function!

* use at least 4 assertions to test your improvements
* (make sure to mix prime and composite numbers in your tests)
"""

import math

def prime(x):
    if x == 2:
        return True
    elif x % 2 == 0:
        return False
    for n in range(3, math.ceil(math.sqrt(x)) + 1):
        if x % n == 0:
            return False
    return True

assert True == prime(11), "11 is a prime number"
assert True == prime(2), "2 is a prime number"
assert False == prime(12), "12 is not a prime number"
assert False == prime(100), "100 is not a prime number"


