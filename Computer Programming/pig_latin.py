"""
pig_latin.py (6 points)
=====

Write a function that translates a word into pig latin

http://en.wikipedia.org/wiki/Pig_Latin

Our version of Pig Latin will follow these rules
-----
* everything automatically gets converted to lowercase (just for implementation
  convenience)
* single letter words remain the same: "a" -> "a"
* any strings with non letter characters (including punctuation, numbers, white
  space) remain the same: "u mad bro" -> "u mad bro", "42" -> "42", "!" -> "!"
* empty string returns empty string: "" -> ""
* words that start with vowels just have "way" appended to them: "at" -> "atway"
* HINT - how to check for vowels?  this sample program does something similar:
  http://foureyes.github.io/csci-ua.0002-spring2015-007/classes/17/review.html#28.0 
* words that start with sh, ch, th or qa have those two letters removed from 
  the beginning of the word, added to the end of the word, with "ay" added at 
  the end: "chillax" -> "illaxchay", "thimble" -> "imblethay"
* all other words (that start with a consonant, are greater than one letter in
  length, and only contain letters) will have the consonant taken away from 
  the front of the word, appended to the end of the word, with "ay" added to 
  the end: "yolo" -> "oloyay", "narwhal" -> "arwhalnay"
* write at least 4 assertions to test your program (use the conditions above as
  a guide)

The function should have the following input and output:
-----
* takes a string as an input  
* returns a string (the pig latin translation of the string)
"""

def pig_latin(string):
    if string.isalpha() == False:
        return string
    elif len(string) < 2:
        return string
    elif string.isalpha() == True:
        lower_string = string.lower()
        first_letter = lower_string[:1]
        first_two_letters = lower_string[:2]
        if first_letter == "a" or first_letter == "e" or first_letter == "i" or first_letter == "o" or first_letter == "u":
            return lower_string + "way"
        elif first_two_letters == "sh" or first_two_letters == "ch" or first_two_letters == "th" or first_two_letters == "qu": #i assume qa in the instructions is qu because no words start with qa
            new_string = lower_string[2:] + first_two_letters + "ay"
            return new_string
        else:
            new_string = string[1:] + first_letter + "ay"
            return new_string


assert "a" == pig_latin("a"), "single letter strings remain the same"
assert "42 " == pig_latin("42 "), "strings with non letter characters remain the same"
assert "atway" == pig_latin("at"), "beginning with vowels, append with way"
assert "imblethay" == pig_latin("thimble"), "beginning with th.. etc append with first 2 letters plus ay"
assert "atcay" == pig_latin("cat"), "words starting with consonants end with first letter plus ay"