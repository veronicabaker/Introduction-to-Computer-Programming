"""
past.py (5 points)
=====
Write a program that asks for 5 present-tense verbs, and prints out
the past-tense version of each verb as they're entered. Follow the
directions below:

* create two functions, one that returns a value, another that does
  not return a value
* create a function called make_past_tense 
  * it should have one parameter, the verb to be changed to
    past-tense
  * it should *return* the past tense version of the verb
  * to make a verb past tense, simply add "ed" to the verb
    * example 1, make_past_tense("walk") --> "walked"
    * example 2, make_past_tense("pack") --> "packed"
  * of course, not all verbs can be made past-tense by adding "ed"
  * ...so make the following exceptions:
    * "run" -> "ran"
    * "drive" -> "drove"
    * "give" -> "gave"
    * "eat" -> "ate"
* create a function called main
  * it should have no parameters
  * it does not return a value
  * within main, use a loop, to ask for 5 verbs
    * prompt the user by asking "Please give me word [number]"
    * after each word entered...
    * use the function that you created to create a past-tense
      version of the word entered
    * print it out saying "The past-tense of [verb] is [new verb]"
* call main

Example Output:
=====
Please give me word #1
> walk
The past-tense of walk is walked.

Please give me word #2
> trick
The past-tense of trick is tricked.

Please give me word #3
> give
The past-tense of give is gave.

Please give me word #4
> watch
The past-tense of watch is watched

Please give me word #5
> drive
The past-tense of drive is drove.
"""
def make_past_tense(verb):
    if verb == "run":
        return "ran"
    elif verb == "drive":
        return "drove"
    elif verb == "give":
        return "gave"
    elif verb == "eat":
        return "ate"
    else:
        return verb + "ed"

def main():
    for i in range(1, 6):
        verb = input("Give me word #%s \n>" %(i))
        past_tense = make_past_tense(verb)
        print("The past tense of %s is %s." %(verb, past_tense))

main()