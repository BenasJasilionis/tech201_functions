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

# Selecting an operation
operation = int(input("Please choose an operation using the following key: 1= Add, 2= Subtract, 3= Divide, 4= Multiply :"))

# If block to choose numbers to be used
if operation != 0:
    num1 = float(input("Choose your first number:"))
    num2 = float(input("Choose your second number:"))

# Main body of the calculator
if operation == 1:
    print(adding(num1, num2))
elif operation == 2:
    print(subtracting(num1, num2))
elif operation == 3:
    print(dividing(num1, num2))
elif operation == 4:
    print(multiplying(num1, num2))

