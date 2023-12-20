# List items are indexed and you can access them by referring to the index number:

# Print the second item of the list:
#             0         1         2
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

"""
Negative indexing means start from the end

-1 refers to the last item, -2 refers to the second last item etc.
"""
#             -3        -2       -1
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

# You can specify a range of indexes by specifying where to start and where to end the range.

# When specifying a range, the return value will be a new list with the specified items.

# Return the third, fourth, and fifth item:
#             0         1         2         3         4      5         6
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

# By leaving out the start value, the range will start at the first item:

print(thislist[:4])

# By leaving out the end value, the range will go on to the end of the list:

print(thislist[2:])

# Specify negative indexes if you want to start the search from the end of the list:

# This example returns the items from "orange" (-4) to, but NOT including "mango" (-1):

#             -7       -6        -5         -4       -3      -2       -1
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

# To determine if a specified item is present in a list use the in keyword:

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")


