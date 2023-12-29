"""
List Comprehension
List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

Example:

Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.

Without list comprehension you will have to write a for statement with a conditional test inside:
"""

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist)

# With list comprehension you can do all that with only one line of code:

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [each for each in fruits if "a" in each]

print(newlist)

# newlist = [expression for item in iterable if condition == True]

numbers = [1, 2, 3, 4, 5, 6, 7]

numbersGreaterThan5 = [each for each in numbers if each > 5];

print(numbersGreaterThan5)

# You can use the range() function to create an iterable:

newlist = [x for x in range(10)]

print(newlist)

names = ["tv", "laptop", "computer"]

newNames=[each.capitalize() for  each in names];

print(newNames)

# The expression can also contain conditions, not like a filter, but as a way to manipulate the outcome:

# Return "orange" instead of "banana":

newlist = [x if x != "banana" else "orange" for x in fruits]

print(newlist)



