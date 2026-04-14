#Write a program to create a function which accepts 2 numbers and one arithmetic operator. Return the answer accordingly.

def calculate(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        if b != 0:
            return a / b
        else:
            return "Division by zero not allowed"
    else:
        return "Invalid operator"


# Taking input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")

# Function call
result = calculate(num1, num2, operator)

# Display result
print("Result:", result)
