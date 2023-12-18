"""
You can return a range of characters by using the slice syntax.

Specify the start index and the end index, separated by a colon, to return a part of the string.
"""
# Get the characters from position 2 to position 5 (not included):
b = "Hello, World!"
print(b[2:5])  # llo

"""
By leaving out the start index, the range will start at the first character:
"""

# Get the characters from the start to position 5 (not included):

b = "Hello, World!"
print(b[:5])  # Hello

"""
By leaving out the end index, the range will go to the end:
"""

# Get the characters from position 2, and all the way to the end:

b = "Hello, World!"
print(b[2:])  # llo, World!

"""
Use negative indexes to start the slice from the end of the string:
"""

# Get the characters:

# rom: "o" in "World!" (position -5)

# To, but not included: "d" in "World!" (position -2):
#
b = "Hello, World!"
print(b[-5:-2])  # orl

