# Simple Calculator in Python

#operator functions
def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y == 0:
        return "Error: Division by zero is not allowed."
    else:
        return x / y

# Main program
# get first number and operator with error handling    
while True:
    try:
        num1 = float(input("Enter the first number: "))
        operator = input("Enter an operator (+, -, *, /): ")
        if operator in ["+", "-", "*", "/"]:
            break
        else:
            print("Invalid operator. Please try again.")
    except ValueError:
        print("Invalid number. Please enter valid numbers.")

# get second number with error handling
while True:
    try:
        num2 = float(input("Enter the second number: "))
        break
    except ValueError:
        print("Invalid number. Please enter valid numbers.")

# if-elif-else statement to perform the calculation    
if operator == "+":
    print("The result is:", round(add(num1, num2), 2))
elif operator == "-":
    print("The result is:", round(subtract(num1, num2), 2))
elif operator == "*":
    print("The result is:", round(multiply(num1, num2), 2))
else:
    print("The result is:", round(divide(num1, num2), 2))