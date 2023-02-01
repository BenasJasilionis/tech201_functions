# Functions

# D R Y
# Don't Repeat Yourself
# The more you repeat yourself, the more complicated your program gets
# Readability decreases
#Better to make it so you dont have to keep r-rewriting the same code, but so you can re-use code

# def = define, followed by the functions name

# the () store arguments
# def print_something():
#     print("Something has been printed")
#
# print_something()

# Functions and arguments

# def print_something(print_string):
#     print(print_string)
#
# print_something("this is my variable")
#
# print_something("This is the second time I called this function")

# In Java:
# public void print_string(String-text)

# Clear naming of arguments is important to increase readability

# def greetings(name):
#     print(f"Hello, my name is {name}")
#
# greetings("Benas")
# greetings("Flo")
# greetings("Luke")
# greetings("Belal")
# greetings("Bakar")

# The Return statement - without return python doesn't hold the value

# def addition(int1, int2):
#     return int1 + int2
#
# print(addition(2, 2))

# Default arguments

# def addition(int1=2, int2=2):
#     return int1 + int2
#
# print(addition())
# print(addition(10, 10))
# print(addition())

# Multiple arguments

# def multi_args(*multiargs):
#     print(type(multiargs))
#
#     for arg in multiargs:
#         print(arg)
#
# multi_args(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# Type Hints

# def greeting(name: str):
#     print("Hello, my name is " + name)
#
# greeting(24601)
# Can specify what data type you want your output to be

# def division(num1: int = 5, num2: int = 2) -> float:
#     return num1 / num2
#
# print(division())

# Function best practices

## Name your functions clearly using lower case and underscores
## All arguments should be clear in their need and where possible include their expected type
## Remember the return statement or functions will return None
## Keep functions small where feasable - for readability and simplicity
## Use comments in your functions/methods to give instructions on how to use them
## Consider using type hints to avoid type errors when you run your code