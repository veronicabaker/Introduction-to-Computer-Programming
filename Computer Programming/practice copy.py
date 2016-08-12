"""
practice.py (4 points)
=====

Follow the instructions below. There are two parts. When you're done with
the file it should be runnable without syntax errors.
"""
print("\n=====\nPart 1: List of lists\n=====")
"""
In this part of the assignment, you will create a list of lists, change an 
element in the list, and print out a list of lists

1. create a variable called nested_lists
2. set that variable equal to an empty list
3. create a loop that loops exactly 3 times
4. within that loop, use the append method on your nested_lists variable to 
   add an entirely new list, [0, 0, 0], as a single element to nested_lists
   on each iteration
5. after the loop, print out the variable, nested_lists; the resulting output 
   should look like this: [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
6. change the value of the 2nd element in the 2nd list to 1
7. loop over every element in your nested_lists variable
8. within your loop print out each element; the output should look something 
   like this:
   [0, 0, 0]
   [0, 1, 0]
   [0, 0, 0]
9. finally, remove the last element in your nested_lists variable using del,
   and print out nested_lists again. this time, the output should look like
   this: [[0, 0, 0], [0, 1, 0]]
"""
# Code for Part 1 goes here

nested_lists = []

for i in range(3):
    nested_lists.append([0, 0, 0])
print(nested_lists)

nested_lists[1][1] = 1

for element in nested_lists:
    print(element)

del nested_lists[len(nested_lists)-1]

print(nested_lists)


print("\n=====\nPart 2: A Function\n=====")
"""
In this part of the assignment, you will create a function that takes in a
list as an argument... and gives back a string based on the instructions
below

1. define a function called create_sentence
2. it should have one parameter, a list called words
3. it will give back a string... composed of the first three letters of all 
   of the words in the list passed in that start with the letter a 
4. in the body of the function...  create an empty string called sentence
5. loop over every element in the list passed in, words
6. if the word starts with the letter a, add the first three letters of the
   word to the string called sentence
7. return the string, sentence
8. call your function and pass it an argument... the argument should be the
   following list: ['bland', 'anxious', 'beetle', 'crass', aardvark']
9. save the result of your function call into a variable and print out the
   result. It should be: "anxaar"
"""

# Code for Part 2 goes here

def create_sentence(words):
    sentence = ""
    for element in words:
        if element[0] == "a":
            sentence += element[:3]
    return sentence

result = create_sentence(["bland", "anxious", "beetle", "crass", "aardvark"])

print(result)
