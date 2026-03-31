# Simple Calculator in Python

#operator functions
def add(x, y):
    return f"The result is: {x + y}"
def subtract(x, y):
    return f"The result is: {x - y}"
def multiply(x, y):
    return f"The result is: {x * y}"
def divide(x, y):
    if y == 0:
        return f"Error: Division by zero is not allowed."
    else:
        return f"The result is: {x / y}"

# Main program
# get first number with error handling    
while True:
    try:
        num1 = float(input("Enter the first number: "))
        break
    except ValueError:
        print("Invalid number. Please enter valid numbers.")
# get operator with error handling
while True:
    operator = input("Enter the operator (+, -, *, /): ")
    if operator in ["+", "-", "*", "/"]:
        break
    else:
        print("Invalid operator. Please enter a valid operator.")

# get second number with error handling
while True:
    try:
        num2 = float(input("Enter the second number: "))
        break
    except ValueError:
        print("Invalid number. Please enter valid numbers.")

# perform calculation based on operator
while operator in ["+", "-", "*"]:
    if operator == "+":
        print(add(num1, num2))
        break
    elif operator == "-":
        print(subtract(num1, num2))
        break
    elif operator == "*":
        print(multiply(num1, num2))
        break
while operator == "/":
    try:
        print(divide(num1, num2))
        break
    except ZeroDivisionError:
        break
