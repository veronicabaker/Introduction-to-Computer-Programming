"""
get_first_word.py (3 points)
=====

Reimplement get_first_word:
2.0http://foureyes.github.io/csci-ua.0002-spring2015-007/classes/17/review.html#3

* instead of using a for loop to get the end index of the word (that 
is.... instead of using a for loop to find the first space character)
* use a string method to search for the first space 
* you can find some potential methods to use in pages 354 through 357 of your
  book
* you can also check the slides: 
  http://foureyes.github.io/csci-ua.0002-spring2015-007/classes/17/objects.html
* keep all four assertions that were in the original slides
"""

def get_first_word(sentence):
    end =sentence.find(" ")
    if end == -1:
        result = sentence
    else:
        result = sentence[:end]
    return result


assert "hi" == get_first_word("hi there!"), "returns first word"
assert "hi" == get_first_word("hi"), "returns word if only one word"
assert "" == get_first_word("    "), "returns empty if only white space"
assert "" == get_first_word(""), "returns empty if sentence is empty"

