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

# Upper case the first letter in this sentence:

txt = "hello, and welcome to my world."

x = txt.capitalize()

print(x)
print(txt)

# The first character is converted to upper case, and the rest are converted to lower case:

txt = "python is FUN!"

x = txt.capitalize()

print(x)

# See what happens if the first character is a number:

txt = "36 is my age."

x = txt.capitalize()

print(x)

# Make the string lower case:

txt = "Hello, And Welcome To My World!"

x = txt.casefold()

print(x)

"""
The casefold() method returns a string where all the characters are lower case.

This method is similar to the lower() method, but the casefold() method is stronger, more aggressive, meaning that it 
will convert more characters into lower case, and will find more matches 
when comparing two strings and both are converted using the casefold() method.
"""

# Print the word "banana", taking up the space of 20 characters, with "banana" in the middle:

txt = "banana"

x = txt.center(20)

print(x)

# The center() method will center align the string, using a specified character (space is default) as the
# fill character.

# Using the letter "O" as the padding character:

txt = "banana"

x = txt.center(20, "O")

print(x)

# Return the number of times the value "apple" appears in the string:
# The count() method returns the number of times a specified value appears in the string.
txt = "I love apples, apple are my favorite fruit"

x = txt.count("apple")

print(x)

# Search from position 10 to 24:

txt = "I love apples, apple are my favorite fruit"

x = txt.count("apple", 7, 20)  # first include last not

print(x)

# Check if the string ends with a punctuation sign (.):

txt = "Hello, welcome to my world."

x = txt.endswith(".")

print(x)


# Check if the string ends with the phrase "my world.":

txt = "Hello, welcome to my world."

x = txt.endswith("my world.")

print(x)

# Check if position 5 to 11 ends with the phrase "my world.":

txt = "Hello, welcome to my world."

x = txt.endswith("my world.", 18, 27)

print(x)

# Set the tab size to 2 whitespaces:

txt = "H\te\tl\tl\to"

x = txt.expandtabs(2)

print(x)


txt = "H\te\tl\tl\to"

print(txt)
print(txt.expandtabs())
print(txt.expandtabs(2))
print(txt.expandtabs(4))
print(txt.expandtabs(10))


# Where in the text is the word "welcome"?:

txt = "Hello, welcome to my world."

x = txt.find("welcome")

print(x)

# Where in the text is the first occurrence of the letter "e"?:

txt = "Hello, welcome to my world."

x = txt.find("e")

print(x)

# Where in the text is the first occurrence of the letter "e" when you only search between position 5 and 10?:

txt = "Hello, welcome to my world."

x = txt.find("e", 5, 10)

print(x)

# If the value is not found, the find() method returns -1, but the index() method will raise an exception:

txt = "Hello, welcome to my world."

print(txt.find("q"))
# print(txt.index("q"))

# Check if all the characters in the text are alphanumeric:

txt = "Company12"

x = txt.isalnum()

print(x)

# Check if all the characters in the text is alphanumeric:

txt = "Company 12"

x = txt.isalnum()

print(x)

# Check if all the characters in the text are letters:

txt = "CompanyX"

x = txt.isalpha()

print(x)

# Check if all the characters in the text is alphabetic:

txt = "Company10"

x = txt.isalpha()

print(x)

# Check if all the characters in a string are decimals (0-9):

txt = "1234"

x = txt.isdecimal()

print(x)

a = "\u0030"  # unicode for 0
b = "\u0047"  # unicode for G

print(a.isdecimal())
print(b.isdecimal())

# Check if all the characters in the text are digits:

txt = "50800"

x = txt.isdigit()

print(x)

a = "\u0030"  # unicode for 0
b = "\u00B2"  # unicode for ²

print(a.isdigit())
print(b.isdigit())

# Check if the string is a valid identifier:

txt = "Demo"

x = txt.isidentifier()

print(x)

# Check if the strings are valid identifiers:

a = "MyFolder"
b = "Demo002"
c = "2bring"
d = "my demo"

print(a.isidentifier())
print(b.isidentifier())
print(c.isidentifier())
print(d.isidentifier())

# Check if all the characters in the text are in lower case:

txt = "hello world!"

x = txt.islower()

print(x)

a = "Hello world!"
b = "hello 123"  # True
c = "mynameisPeter"

print(a.islower())
print(b.islower())
print(c.islower())


# Check if all the characters in the text are numeric:

txt = "565543"

x = txt.isnumeric()

print(x)

"""
The isnumeric() method returns True if all the characters are numeric (0-9), otherwise False.

Exponents, like ² and ¾ are also considered to be numeric values.

"-1" and "1.5" are NOT considered numeric values, because all the characters in the string must be numeric, and the - and the . are not.
"""

a = "\u0030"  # unicode for 0
b = "\u00B2"  # unicode for &sup2;
c = "10km2"
d = "-1"
e = "1.5"

print(a.isnumeric())  # True
print(b.isnumeric())  # True
print(c.isnumeric())
print(d.isnumeric())  # False
print(e.isnumeric())  # False

# Check if all the characters in the text are printable:

txt = "Hello! Are you #1?"

x = txt.isprintable()

print(x)

"""
The isprintable() method returns True if all the characters are printable, otherwise False.

Example of none printable character can be carriage return and line feed.
"""

txt = "Hello!\nAre you #1?"

x = txt.isprintable()

print(x)

# Check if all the characters in the text are whitespaces:

txt = "   "

x = txt.isspace()

print(x)

txt = "   s   "

x = txt.isspace()

print(x)

# Check if each word start with an upper case letter:
"""
The istitle() method returns True if all words in a text start with a upper case letter, AND the rest of the word 
are lower case letters, otherwise False.

Symbols and numbers are ignored.
"""

txt = "Hello, And Welcome To My World!"

x = txt.istitle()

print(x)

# Check if each word start with an upper case letter:

a = "HELLO, AND WELCOME TO MY WORLD"  # false
b = "Hello"  # True
c = "22 Names"  # True
d = "This Is %'!?"  # True

print(a.istitle())
print(b.istitle())
print(c.istitle())
print(d.istitle())


# Check if all the characters in the text are in upper case:

txt = "THIS IS NOW!"

x = txt.isupper()

print(x)

"""
The isupper() method returns True if all the characters are in upper case, otherwise False.

Numbers, symbols and spaces are not checked, only alphabet characters.
"""
a = "Hello World!"
b = "hello 123"
c = "MY NAME IS PETER 1"

print(a.isupper())
print(b.isupper())
print(c.isupper())  # True

# Join all items in a tuple into a string, using a hash character as separator:

myTuple = ("John", "Peter", "Vicky")

x = "#".join(myTuple)

print(x)

"""
The join() method takes all items in an iterable and joins them into one string.

A string must be specified as the separator.
"""

# Join all items in a dictionary into a string, using the word "TEST" as separator:


myDict = {"name": "John", "country": "Norway"}
mySeparator = "TEST"

x = mySeparator.join(myDict)

print(x)  # nameTESTcountry


# Return a 20 characters long, left justified version of the word "banana":

txt = "banana"

x = txt.ljust(20)

print(x, "is my favorite fruit.")

# The ljust() method will left align the string, using a specified character (space is default) as the fill character.
# Using the letter "O" as the padding character:

txt = "banana"

x = txt.ljust(20, "O")

print(x)


# Lower case the string:


txt = "Hello my FRIENDS"

x = txt.lower()

print(x)

# Remove spaces to the left of the string:

txt = "     banana     "

x = txt.lstrip()

print("of all fruits", x, "is my favorite")

# Remove the leading characters:

txt = ",,,,,ssaaww.....banana"

x = txt.lstrip(",.asw")  # banana

print(x)  # banana

# Create a mapping table, and use it in the translate() method to replace any "S" characters with a "P" character:

txt = "Hello Sam!"
mytable = str.maketrans("S", "P")
print(txt.translate(mytable))

"""
The maketrans() method returns a mapping table that can be used with the translate() method to replace specified characters.
"""



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

# The maketrans() method itself returns a dictionary describing each replacement, in unicode:

txt = "Good night Sam!"
x = "mSa"
y = "eJo"
z = "odnght"
print(str.maketrans(x, y, z))














