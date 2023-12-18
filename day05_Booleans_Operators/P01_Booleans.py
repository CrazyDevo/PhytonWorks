"""

In programming you often need to know if an expression is True or False.

You can evaluate any expression in Python, and get one of two answers, True or False.

When you compare two values, the expression is evaluated and Python returns the Boolean answer:
"""
print(10 > 9)
print(10 == 9)
print(10 < 9)

# Print a message based on whether the condition is True or False:

a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")


# The bool() function allows you to evaluate any value, and give you True or False in return,

# Evaluate a string and a number:

print(bool("Hello"))  # True
print(bool(15))  # True

x = "Hello"
y = 15

print(bool(x))
print(bool(y))

"""
Almost any value is evaluated to True if it has some sort of content.

Any string is True, except empty strings.

Any number is True, except 0.

Any list, tuple, set, and dictionary are True, except empty ones.
"""

bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

# In fact, there are not many values that evaluate to False, except empty values, such as (), [], {}, "",
# the number 0, and the value None. And of course the value False evaluates to False.

# The following will return False:

bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

# Python also has many built-in functions that return a boolean value, like the isinstance() function, which
# can be used to determine if an object is of a certain data type:

# Check if an object is an integer or not:

x = 200
print(isinstance(x, int))


