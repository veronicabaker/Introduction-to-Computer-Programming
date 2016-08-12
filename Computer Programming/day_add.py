"""
day_add.py (6 points)
=====
From How to Think Like a Computer Scientist, Chapter 6 Exercises:

http://openbookproject.net/thinkcs/python/english3e/fruitful_functions.html#exercises

Write a function that helps answer questions like '"Today is Wednesday. I leave on holiday in 19 days time. What day will that be?"' ...So the function must take a day name and a delta argument — the number of days to add — and should return the resulting day name:

day_add("Monday", 4)   # returns "Friday"
day_add("Tuesday", 0)  # returns "Tuesday"
day_add("Tuesday", 14) # returns "Tuesday"
day_add("Sunday", 100) # returns "Tuesday"

Write assertions to test the above examples.
"""

#hint: break into functions day to number, number to day

def day_to_number(day):
    if day == "Monday":
        n = 1
    elif day == "Tuesday":
        n = 2
    elif day == "Wednesday":
        n = 3
    elif day == "Thursday":
        n = 4
    elif day == "Friday":
        n = 5
    elif day == "Saturday":
        n = 6
    elif day == "Sunday":
        n = 7
    return n

def number_to_day(n):
    day = ""
    if n == 1:
        day += "Monday"
    elif n == 2:
        day += "Tuesday"
    elif n == 3:
        day += "Wednesday"
    elif n == 4:
        day += "Thursday"
    elif n == 5:
        day += "Friday"
    elif n == 6:
        day += "Saturday"
    elif n == 7:
        day += "Sunday"
    return day


def day_add(day, delta):
    position = delta % 7
    start = day_to_number(day)
    position += start
    if position > 7:
        position_2 = position % 7
        position = position_2
    result = number_to_day(position)
    return result


assert "Friday" == day_add("Monday", 4), "4 days from Monday is a Friday"
assert "Tuesday" == day_add("Tuesday", 0), "0 days from Tuesday is a Tuesday"
assert "Tuesday" == day_add("Tuesday", 14), "12 days from Tuesday is a Tuesday"
assert "Tuesday" == day_add("Sunday", 100), "100 days from Sunday is a Tuesday"

