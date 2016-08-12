"""
multiples_of_seven.py (3 points)
=====

* create a function called multiples_of_seven
* it should take a list of numbers as an argument (don't worry about lists
  with non-numeric data)
* it should return a *new* list with only numbers that are multiples of 7
* if there are no multiples of seven, return an empty list ([])
* come up with two assertions to test this

Example Output:
-----
print(multiples_of_seven([80, 49, 70, 125]))
[49, 70]

Hint:
Create a new list... and use a method called append to add elements to it!
my_list.append(number)
"""

def multiples_of_seven(numbers):
    new_list = []
    for i in numbers:
        if i % 7 == 0:
            new_list.append(i)
    return new_list

assert [] == multiples_of_seven([1, 2, 3]), "return empty list if no multiples of 7"
assert [49, 70] == multiples_of_seven([80, 49, 70, 125]), "returns list of multiples of 7"

print(multiples_of_seven([80, 49, 70, 125]))