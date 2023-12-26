# You can loop through the list items by using a for loop:

thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)

# You can also loop through the list items by referring to their index number.

# Use the range() and len() functions to create a suitable iterable.

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
    print(thislist[i])

"""
You can loop through the list items by using a while loop.

Use the len() function to determine the length of the list, then start at 0 and loop your way through the list items 
by referring to their indexes.

Remember to increase the index by 1 after each iteration.
"""

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
    print(thislist[i])
    i = i + 1

# List Comprehension offers the shortest syntax for looping through lists:

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

