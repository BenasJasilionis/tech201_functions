# tech201_functions

# Functions
The purpose of using functions is to follow D.R.Y : Dont, Repeat, Yourself
* The more you repeat yourself, the more complicated your program gets, which decreases readability
* Functions also make your code re-usable, so you don't have to keep re-writing lines of code every time you want to change a parameter

### Anatomy of a function
A function is created with the following syntax : `def function_name(arguments)`
1) The `def` phrase is the initiation of a function
2) The `function_name` is what your function will be called
3) The `(arguments)` can either be left empty, or specified with variables to utilise the true power of functions

### Basic functions
````python
def print_something():
    print("Something has been printed")

print_something()
# Output = Something has been printed
````
* Functions are activated by typing their name in a separate line after defining them, this is called `calling` a function
* Because the above function has no `parameters` (nothing in the `()`), whenever it is `called` it gives the same output

### Functions and arguments
````python
def print_something(print_string):
    print(print_string)
````
* Because this function has a `parameter`, when calling this function something must be passed in the `()` otherwise an error will occur
* With the above code, whatever `argument` is entered when calling it is what will be printed out
````python
def greetings(name):
    print(f"Hello, my name is {name}")
    
greetings("Benas") # Output = Hello, my name is Benas
greetings("Josh")  # Output = Hello, my name is Josh
greetings("Luke")  # Output = Hello, my name is Luke
greetings("Jake")  # Output = Hello, my name is Jake
greetings("Jordan") # output = Hello, my name is Jordan
````
* The above example highlights how functions can save time
* Instead of manually printing out the string `Hello, my name is {name}` for each person, we can simply call the function with the persons name, and it will do most of the work for us

### The return statement
Functions do not store the data they handle in a visible form, unless you tell them to `return` their output:
````python
def addition(int1, int2):
    return int1 + int2

print(addition(2, 2)) # Output = 4
````
* Here we see a function which adds two numbers together
* If we were to try and `call` the function without the `return` argument, we would get back `None`, since there is nothing in the function which would allow us to visualise the output
* Instead, we can tell the function to `return` the output, so that when we print it we see the expected output of `4`

**Important note**- a function needs to be printed in order to visualise the output if there is nothing within the function which would cause data to be displayed in the terminal, e.g. no print statements.

### Default arguments
* Function `parameters` can be given default values which will be used if the function is called with no `arguments`
* The syntax for this is : `def function(var1="default string")`
````python
def addition(int1=2, int2=2):
    return int1 + int2

print(addition())       # Output = 4
print(addition(10, 10)) # Output = 20
````
* In the above function, the two `parameters` are both set to `= 2`, so that if the function is called with no `arguments` it uses those default values, and outputs `4`
* However, even when default values are set, the function can be called with `arguments` which overwrite the default values as can be seen the second time the function is called

### Multiple arguments
Until now, each function we have created has either had no `parameters` or a hard coded number of `parameters`, however functions can be made to have multiple `arguments` with the syntax : `def function(*multiargs):` where the `*` signifies multiple `arguments`.

````python
def multi_args(*multiargs):
    print(type(multiargs))  # Output = class tuple

    for arg in multiargs:
        print(arg)

multi_args(1, 2, 3, 4, 5, 6, 7, 8, 9, 10) # Output = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
````
* As can be seen, using the `*` to allow for multiple `arguments` causes the function to create a `tuple`
* The `for` loop is there simply to highlight that multiple `arguments` have been passed, this can be seen in the output

### Type hints - variables
In order to avoid `type errors`, functions can be made to warn the user when an `argument` of an incorrect `type` is being passed using the syntax: `def function(var1 :datatype(e.g. int)):`
````python
def greeting(name: str):
    print("Hello, my name is " + name)
    
greeting(24601)
````
* For example, if we have a function which greets someone with their name, we want the user to input a `string` as an argument.
* By using the `: str`, when we go to call `greeting()`, the program will highlight our `argument` if it is of an inappropriate datatype as is the case in the example

# Type hints - outputs
We can also tell the function what sort of output we want from function, to make sure that the `arguments` which we pass can give that output. This is done by having a ` -> "datatype":` after the `parameters`
````python
def division(num1: int = 5, num2: int = 2) -> float:
    return num1 / num2

print(division()) # Output = 2.5
````
* In the above example, the output will be `2.5`, however any combination of numbers could be used and the output would still be presented in the `float` type.

### Functions best practice
1) Name your functions clearly using lower case and underscores
2) All arguments should be clear in their need and where possible include their expected type
3) Remember the return statement or functions will return None 
4) Keep functions small where feasable - for readability and simplicity 
5) Use comments in your functions/methods to give instructions on how to use them 
6) Consider using type hints to avoid type errors when you run your code

# Making a simple calculator
1) Define the functions for the 4 operations: -, +, *, /:
````python
# Adding
def adding(x, y) -> float:
    return x + y

# Subtracting
def subtracting(x, y) -> float:
    return x - y

# Dividing
def dividing(x, y) -> float:
    return x / y

# Multiplying
def multiplying(x, y) -> float:
    return x * y
````
2) Define a variable which will store the users chosen operation:
````python
# Selecting an operation
operation = int(input("Please choose an operation using the following key: 1= Add, 2= Subtract, 3= Divide, 4= Multiply :"))
````
3) Create an `if` block to allow the user to choose 2 numbers for the operation:
````python
if operation != 0:
    num1 = float(input("Choose your first number:"))
    num2 = float(input("Choose your second number:"))
````
4) Create an `if` block which will call the various functions based on the users input:
````python
if operation == 1:
    print(adding(num1, num2))
elif operation == 2:
    print(subtracting(num1, num2))
elif operation == 3:
    print(dividing(num1, num2))
elif operation == 4:
    print(multiplying(num1, num2))
````



