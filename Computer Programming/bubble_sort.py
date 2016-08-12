"""
bubble_sort.py (8 points)
-----

Oops!  The makers of Python inadvertently removed the ability to sort using 
the sort method.  Uh-oh.  Looks like you'll need to write your own way to sort
lists.  Instead of using a method, you decide to write a function called
bubble_sort.

Your bubble_sort function:

* will take one argument, a list of numbers.  
* will return a list with all of the elements sorted
* you will use the bubble sort algorithm to manually sort the list (see the 
  wikipedia article: http://en.wikipedia.org/wiki/Bubble_sort):
	* go through every element in the list
	* compare that element to the element adjacent to it 	
	* swap the two if the second element is less than the first
	* once you reach the end, start over and do the same thing again
	* keep on repeating until you through the entire list without swapping
* test your code... for example:
	* bubble_sort([4, 5, 1]) returns [1, 4, 5]
	* bubble_sort([1, 1, 1]) returns [1, 1, 1]
	* bubble_sort([2]) returns [2]
	* bubble_sort([9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2]) 
	  returns [-2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
* you must use iterating with indexes! 
* the following slides are a good reference:

http://foureyes.github.io/csci-ua.0002-spring2015-007/classes/23/iterating_with_indexes.html

From the wikipedia article, here's an example of the algorithm at work:

First Pass:
( 5 1 4 2 8 )  ( 1 5 4 2 8 ), Here, algorithm compares the first two elements, and swaps since 5 > 1.
( 1 5 4 2 8 )  ( 1 4 5 2 8 ), Swap since 5 > 4
( 1 4 5 2 8 )  ( 1 4 2 5 8 ), Swap since 5 > 2
( 1 4 2 5 8 )  ( 1 4 2 5 8 ), Now, since these elements are already in order (8 > 5), algorithm does not swap them.
Second Pass:
( 1 4 2 5 8 )  ( 1 4 2 5 8 )
( 1 4 2 5 8 )  ( 1 2 4 5 8 ), Swap since 4 > 2
( 1 2 4 5 8 )  ( 1 2 4 5 8 )
( 1 2 4 5 8 )  ( 1 2 4 5 8 )
Now, the array is already sorted, but our algorithm does not know if it is completed. The algorithm needs one whole pass without any swap to know it is sorted.
Third Pass:
( 1 2 4 5 8 )  ( 1 2 4 5 8 )
( 1 2 4 5 8 )  ( 1 2 4 5 8 )
( 1 2 4 5 8 )  ( 1 2 4 5 8 )
( 1 2 4 5 8 )  ( 1 2 4 5 8 )
"""

def bubble_sort(numbers):
    keep_sorting = True
    while keep_sorting == True:
        previous_value = numbers[0]
        keep_sorting = False
        for i in range(len(numbers)):
            current_value = numbers[i]
            if previous_value > current_value:
                numbers[i] = previous_value
                numbers[i-1] = current_value
                keep_sorting = True
            else:
                previous_value = current_value
    return numbers

assert [1, 4, 5] == bubble_sort([4, 5, 1])
assert [1, 1, 1,] == bubble_sort([1, 1, 1])
assert [2] == bubble_sort([2])
assert [-2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9] == bubble_sort([9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2])