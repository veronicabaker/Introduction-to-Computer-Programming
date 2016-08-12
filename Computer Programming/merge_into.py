"""
merge_into.py - 5 points
=====

Write a function called merge_into... it'll merge all of the items from one
list into another list (as long as the item doesn't already exist).

* it will have two lists as parameters:
  * dest
  * source
* it will go over every element from source
* if the element doesn't exist in dest yet, then add it to dest
* return dest

Examples:
print(merge_into([1, 2], [3, 4])) # --> [1, 2, 3, 4]
print(merge_into([1, 2], [1, 2])) # --> [1, 2]
print(merge_into([1, 2, 3, 4], [2, 4, 6, 8])) # --> [1, 2, 3, 4, 6, 8]
print(merge_into([1], [2, 2, 2])) # --> [1, 2]
"""

def merge_into(dest, source):
    for element in source:
        if element not in dest:
            dest.append(element)
    return dest

assert [1, 2, 3, 4] == merge_into([1, 2], [3, 4])
assert [1, 2] == merge_into([1, 2], [1, 2])
assert [1, 2, 3, 4, 6, 8] == merge_into([1, 2, 3, 4], [2, 4, 6, 8])
assert [1, 2] == merge_into([1], [2, 2, 2])