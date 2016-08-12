"""
n3rd_talk.py (9 points)
=====

Write a function that converts a word into "1337" speak. Use
assertions to test your function.

http://en.wikipedia.org/wiki/Leet

We'll use a simple variant that follows these rules:
-----
* the vowels 'A', 'E', 'I', and 'O', regardless of case will be converted into
  the numbers '/\\', '3', '1', '0' (this should only print out with one back-
  slash)
* all other letters are converted to uppercase
* punctuation and spacing are left as is
* empty string returns empty string

Use assertions to test the following:
-----
* an empty string should give back a string
* "androids inside!  do not enter!" should give back:
  "/\\NDR01DS 1NS1D3!  D0 N0T 3NT3R!"
* "aeioAEIO" should give back: "/\\310/\\310" (this should only print out with
  one backslash each)
* add any other tests that you think are appropriate

Output
-----
* finally (after the asserts), create a variable called result
* assign the result of calling your function on the string:
  "An amazing assignment."
* print out the variable, result

IPO
-----
* input: takes a string to be converted as an input  
* processing: substitute letters according to the rules above
* output: returns the 1337 speak version of the original string

Hints:
-----
* start with an empty string
* accumulate letters into that string
* use conditionals to determine whether or not a substitution should take
  place
* a is a special case, as its substitution consists of two characters
* one of those characters requires an escape sequence (remember strings from
  earlier in the semester?), which is why there are two backslashes in a row
"""

def n3rd_talk(string):
    converted_string = ""
    for i in string:
        if i == "A" or i == "a":
            converted_string += "/\\"
        elif i == "e" or i == "E":
            converted_string += "3"
        elif i == "I" or i == "i":
            converted_string += "1"
        elif i == "o" or i == "O":
            converted_string += "0"
        else:
            converted_string += i.upper()
    return converted_string

assert "" == n3rd_talk(""), "an empty string should give back a string"
assert "/\\NDR01DS 1NS1D3! D0 N0T 3NT3R!" == n3rd_talk("androids inside! Do not enter!"), "androids inside! Do not enter! should return /\\NDR01DS 1NS1D3!  D0 N0T 3NT3R!"
assert "/\\310/\\310" == n3rd_talk("aeioAEIO"), "aeioAEIO should give back: /\\310/\\310"

result = n3rd_talk("An amazing assignment.")

print(result)