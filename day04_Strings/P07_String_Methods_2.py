"""
Python has a set of built-in methods that you can use on strings.
Note: All string methods return new values. They do not change the original string.


Method	                    Description
capitalize()	            Converts the first character to upper case
casefold()	                Converts string into lower case
center()	                Returns a centered string
count()	                    Returns the number of times a specified value occurs in a string
encode()	                Returns an encoded version of the string
endswith()	                Returns true if the string ends with the specified value
expandtabs()	            Sets the tab size of the string
find()	                    Searches the string for a specified value and returns the position of where it was found
format()	                Formats specified values in a string
format_map()	            Formats specified values in a string
index()	                    Searches the string for a specified value and returns the position of where it was found
isalnum()	                Returns True if all characters in the string are alphanumeric
isalpha()	                Returns True if all characters in the string are in the alphabet
isascii()	                Returns True if all characters in the string are ascii characters
isdecimal()	                Returns True if all characters in the string are decimals
isdigit()	                Returns True if all characters in the string are digits
isidentifier()	            Returns True if the string is an identifier
islower()	                Returns True if all characters in the string are lower case
isnumeric()	                Returns True if all characters in the string are numeric
isprintable()	            Returns True if all characters in the string are printable
isspace()	                Returns True if all characters in the string are whitespaces
istitle()	                Returns True if the string follows the rules of a title
isupper()	                Returns True if all characters in the string are upper case
join()	                    Joins the elements of an iterable to the end of the string
ljust()                 	Returns a left justified version of the string
lower()	                    Converts a string into lower case
lstrip()	                Returns a left trim version of the string
maketrans()	                Returns a translation table to be used in translations
partition()	                Returns a tuple where the string is parted into three parts
replace()	                Returns a string where a specified value is replaced with a specified value
rfind()	                    Searches the string for a specified value and returns the last position of where it was found
rindex()	                Searches the string for a specified value and returns the last position of where it was found
rjust()	                    Returns a right justified version of the string
rpartition()	            Returns a tuple where the string is parted into three parts
rsplit()	                Splits the string at the specified separator, and returns a list
rstrip()	                Returns a right trim version of the string
split()	                    Splits the string at the specified separator, and returns a list
splitlines()	            Splits the string at line breaks and returns a list
startswith()	            Returns true if the string starts with the specified value
strip()	                    Returns a trimmed version of the string
swapcase()	                Swaps cases, lower case becomes upper case and vice versa
title()	                    Converts the first character of each word to upper case
translate()	                Returns a translated string
upper()	                    Converts a string into upper case
zfill()	                    Fills the string with a specified number of 0 values at the beginning
"""


"""
Search for the word "bananas", and return a tuple with three elements:

1 - everything before the "match"
2 - the "match"
3 - everything after the "match"
"""
txt = "I could eat bananas all day"

x = txt.partition("bananas")

print(x)

"""
The partition() method searches for a specified string, and splits the string into a tuple containing three elements.

The first element contains the part before the specified string.

The second element contains the specified string.

The third element contains the part after the string.
"""

# If the specified value is not found, the partition() method returns a tuple containing:
# 1 - the whole string, 2 - an empty string, 3 - an empty string:

txt = "I could eat bananas all day"

x = txt.partition("apples")

print(x)

# Replace the word "bananas":

txt = "I like bananas"

x = txt.replace("bananas", "apples")

print(x)

# Note: All occurrences of the specified phrase will be replaced, if nothing else is specified.

# Replace all occurrence of the word "one":

txt = "one one was a race horse, two two was one too."

x = txt.replace("one", "three")

print(x)

# Replace the two first occurrence of the word "one":

txt = "one one was a race horse, two two was one too."

x = txt.replace("one", "three", 2)

print(x)

# Where in the text is the last occurrence of the string "casa"?:

txt = "Mi casa, su casa."

x = txt.rfind("casa")

print(x)


"""
The rfind() method finds the last occurrence of the specified value.

The rfind() method returns -1 if the value is not found.

The rfind() method is almost the same as the rindex() method. See example below.
"""

txt = "Hello, welcome to my world."

x = txt.rfind("e")

print(x)

# Where in the text is the last occurrence of the letter "e" when you only search between position 5 and 10?:

txt = "Hello, welcome to my world."

x = txt.rfind("e", 5, 10)

print(x)

# If the value is not found, the rfind() method returns -1, but the rindex() method will raise an exception:


txt = "Hello, welcome to my world."

print(txt.rfind("q"))
#  print(txt.rindex("q"))

# Return a 20 characters long, right justified version of the word "banana":


txt = "banana"

x = txt.rjust(20)

print(x, "is my favorite fruit.")

# The rjust() method will right align the string, using a specified character (space is default) as the fill character.


txt = "banana"

x = txt.rjust(20, "O")

print(x)

# Search for the last occurrence of the word "bananas", and return a tuple with three elements:
#
# 1 - everything before the "match"
# 2 - the "match"
# 3 - everything after the "match"


txt = "I could eat bananas all day, bananas are my favorite fruit"

x = txt.rpartition("bananas")

print(x)

# If the specified value is not found, the rpartition() method returns a tuple containing:
# 1 - an empty string, 2 - an empty string, 3 - the whole string:

txt = "I could eat bananas all day, bananas are my favorite fruit"

x = txt.rpartition("apples")

print(x)

# Split a string into a list, using comma, followed by a space (, ) as the separator:

txt = "apple, banana, cherry"

x = txt.rsplit(", ")

print(x)

"""
The rsplit() method splits a string into a list, starting from the right.

If no "max" is specified, this method will return the same as the split() method.

Note: When maxsplit is specified, the list will contain the specified number of elements plus one.
"""

txt = "apple, banana, cherry"

# setting the maxsplit parameter to 1, will return a list with 2 elements!
x = txt.rsplit(", ", 1)

print(x)

# Split a string into a list where each word is a list item:

txt = "welcome to the jungle"

x = txt.split()

print(x)

"""
The split() method splits a string into a list.

You can specify the separator, default separator is any whitespace.
"""
# When maxsplit is specified, the list will contain the specified number of elements plus one.


# Split the string, using comma, followed by a space, as a separator:


txt = "hello, my name is Peter, I am 26 years old"

x = txt.split(", ")

print(x)

# Use a hash character as a separator:

txt = "apple#banana#cherry#orange"

x = txt.split("#")

print(x)

# Split the string into a list with max 2 items:

txt = "apple#banana#cherry#orange"

# setting the maxsplit parameter to 1, will return a list with 2 elements!
x = txt.split("#", 1)

print(x)

# Split a string into a list where each line is a list item:

txt = "Thank you for the music\nWelcome to the jungle"

x = txt.splitlines()

print(x)

# The splitlines() method splits a string into a list. The splitting is done at line breaks.

# Split the string, but keep the line breaks:
# keeplinebreaks	Optional. Specifies if the line breaks should be included (True), or not (False).
# Default value is False
txt = "Thank you for the music\nWelcome to the jungle"

x = txt.splitlines(True)

print(x)

# Check if the string starts with "Hello":

txt = "Hello, welcome to my world."

x = txt.startswith("Hello")

print(x)

# Check if position 7 to 20 starts with the characters "wel":


txt = "Hello, welcome to my world."

x = txt.startswith("wel", 7, 10)

print(x)

# Remove spaces at the beginning and at the end of the string:

txt = "     banana     "

x = txt.strip()

print("of all fruits", x, "is my favorite")


"""
The strip() method removes any leading, and trailing whitespaces.

Leading means at the beginning of the string, trailing means at the end.

You can specify which character(s) to remove, if not, any whitespaces will be removed.
"""

# Remove the leading and trailing characters:

txt = ",,,,,rrttgg.....banana....rrr"

x = txt.strip(",.grt")

print(x)

# Make the lower case letters upper case and the upper case letters lower case:
# The swapcase() method returns a string where all the upper case letters are lower case and vice versa.

txt = "Hello My Name Is PETER"

x = txt.swapcase()

print(x)

# Make the first letter in each word upper case:

txt = "Welcome to my world"

x = txt.title()

print(x)

"""
The title() method returns a string where the first character in every word is upper case. Like a header, or a title.

If the word contains a number or a symbol, the first letter after that will be converted to upper case.
"""
# Make the first letter in each word upper case:

txt = "Welcome to my 2nd world"

x = txt.title()  # Welcome To My 2Nd World

print(x)

# Note that the first letter after a non-alphabet letter is converted into a upper case letter:

txt = "hello b2b2b2 and 3g3g3g"

x = txt.title()  # Hello B2B2B2 And 3G3G3G

print(x)

# Replace any "S" characters with a "P" character:

# use a dictionary with ascii codes to replace 83 (S) with 80 (P):
mydict = {83:  80}
txt = "Hello Sam!"
print(txt.translate(mydict))

"""
The translate() method returns a string where some specified characters are replaced with the character described in 
a dictionary, or in a mapping table.

Use the maketrans() method to create a mapping table.

If a character is not specified in the dictionary/table, the character will not be replaced.

If you use a dictionary, you must use ascii codes instead of characters.
"""

# Use a mapping table to replace "S" with "P":

txt = "Hello Sam!"
mytable = str.maketrans("S", "P")
print(txt.translate(mytable))

# Use a mapping table to replace many characters:

txt = "Hi Sam!"
x = "mSa"
y = "eJo"
mytable = str.maketrans(x, y)
print(txt.translate(mytable))

# The third parameter in the mapping table describes characters that you want to remove from the string:

txt = "Good night Sam!"
x = "mSa"
y = "eJo"
z = "odnght"
mytable = str.maketrans(x, y, z)
print(txt.translate(mytable))

# The same example as above, but using a dictionary instead of a mapping table:

txt = "Good night Sam!"
mydict = {109: 101, 83: 74, 97: 111, 111: None, 100: None, 110: None, 103: None, 104: None, 116: None}
print(txt.translate(mydict))

# Upper case the string:

txt = "Hello my friends"

x = txt.upper()

print(x)

"""
The upper() method returns a string where all characters are in upper case.

 Symbols and Numbers are ignored.
"""

# Fill the string with zeros until it is 10 characters long:

txt = "50"

x = txt.zfill(10)

print(x)

"""
The zfill() method adds zeros (0) at the beginning of the string, until it reaches the specified length.

If the value of the len parameter is less than the length of the string, no filling is done.
"""

# Fill the strings with zeros until they are 10 characters long:


a = "hello"
b = "welcome to the jungle"
c = "10.000"

print(a.zfill(10))
print(b.zfill(10))
print(c.zfill(10))