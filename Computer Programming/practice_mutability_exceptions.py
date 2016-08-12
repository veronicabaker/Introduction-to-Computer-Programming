"""
practice_mutability_exceptions.py (3 points)
=====
Write code under each comment (below the #####'s). This file should be 
runnable without syntax errors.
"""

# PART 1
# -----
# Create a variable called cats and set it equal to the following list:
#
# ['mungo', 'heathcliff', 'riff-raff']
#####

cats = ['mungo', 'heathcliff', 'riff-raff']

# Create a variable called copy_cats, and set it equal to cats
# ... simply do this: copy_cats = cats
#####

copy_cats = cats

# Using append, add another cat, named 'wordsworth', to copy_cats
#####

copy_cats.append('wordsworth')

# Print out both cats and copy_cats
#####

print(cats)
print(copy_cats)

# Print out a message saying what you observed about the two variables
#####

print("cats and copy_cats are the same")

# PART 2
# -----
# Now... create a new list called numbers, and set it equal to [1, 2, 3]
#####

numbers = [1, 2, 3]

# Create a function called remove_first. It should take one parameter, my_list.
# It should not return any value.
# It should use del to remove the 1st element of my_list
#####

def remove_first(my_list):
    del my_list[0]

# Call your remove_first function by passing it your list from above, numbers.
#####

remove_first(numbers)

# Print out numbers... and print out a message explaining what happened.
#####

print(numbers)
print("numbers has been mutated by the function and is now [2, 3]")

# PART 3
# -----
# Now... try to print out the element at index 100 of your cats list
# (it should give you an error after you run this file)
#####

#print(cats[100])

# MODIFY THE ABOVE CODE with a try/except statement so that you "catch"
# the IndexError in the except clause. Within your except clause, print out
# a message saying: "nope, not here!". Make sure this file is runnable when
# you've completed this last part (that is, the exception is handled by your
# except clause).

try:
    print(cats[100])
except:
    print("nope, not here!")

#####
