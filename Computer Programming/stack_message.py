"""
stack_message.py - 7 points
=====
Your super paranoid friend just sent you a secret message. She said that
you'll need to write a program to decode it! Her instructions are as
follows:


* Write a function that takes a single string, my message, as an argument.
* First keep track of a decoded message (there's nothing in it yet!).
* Go through every character in my message...
  * If the character is an uppercase letter, or if it's a space...
    * Add the letter to a list.
  * However, if it's an asterisk, and there's at least 1 letter in your list...
    * Remove the last letter that you placed in your list and add it to the
      decoded message.
  * If the character is any other character, you don't have to do anything
* Once you're done, you should have my decoded message!
* Your function should return the resulting message
* Finally, call your function on my secret message:

"OW** What!?**US***C*. cH**ES**C*TER*****Craaa?"

Hint: the result should be three words, all uppercase, the first word is three
      letters, the second is four, and the last is six
Hint: start with an empty list
Hint: append would be useful for adding to a list
Hint: pop would be useful for removing the last element in a list
Hint: make sure you that you check your list before you pop off an element
"""

def stack_message(message):
    decoded_message = ""
    new_list = []
    for c in message:
        if c.isupper() == True or c == " ":
            new_list.append(c)
        elif c == "*" and len(new_list) > 0:
            decoded_message += new_list.pop()
    return decoded_message

print(stack_message("OW** What!?**US***C*. cH**ES**C*TER*****Craaa?"))

