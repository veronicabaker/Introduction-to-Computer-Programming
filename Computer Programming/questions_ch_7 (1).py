"""
questions_ch_7.py - 4 points
=====
* answer the following questions below
* type out the answers to each question within the comment, underneath the 
  dashed line: ----- 
"""

"""
1. (1/2 point) Write two ways to get the last element in a list through 
indexing.
-----

list[-1]
list[len(list) - 1]

2. (1/2 point) Is a list mutable or immutable?
-----

mutable

3. (1 point) What does the following print out?
-----
new_list = ['a', 'b'] + ['b', 'c']
print(new_list.count('b'))
print(new_list.index('b'))

2
1


4. (1/2 point) In code, show two ways to get rid of the number 8 from this list [0, -3, 12, 8]
-----

del list[-1]
list.remove(8)

5. (1 point) Version 1 of the code below uses append; version 2 uses extend. What is printed out for each version? Why?

# version 1
numbers = [1, 2, 3]
numbers.append([4, 5])
print(numbers)

# version 2
numbers = [1, 2, 3]
numbers.extend([4, 5])
print(numbers)
-----

version one adds the list [4, 5] into the list numbers so that the output is [1, 2, 3, [4, 5]]
version 2 adds each element of the iterable object (list) to the end of numbers so the output is [1, 2, 3, 4, 5]

6. (1/2 point) Name 2 list methods other than append, extend, or remove and *briefly* describe what they do.
-----

insert: takes an item and a position and adds the item to that position in a list
pop: removes and returns the last element in a list

"""
