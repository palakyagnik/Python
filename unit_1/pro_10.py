#Write a program to create 4 lambda functions which shall accept 2 numbers and one arithmetic operator. As per arithmetic operator related lambda functions shall be invoked.

add = lambda a,b : a+b
sub = lambda a,b : a-b
mul = lambda a,b : a*b
div = lambda a, b: a / b if b != 0 else "Cannot divide by zero"

num1 = float(input("Enter first number:"))
num2 = float(input("Enter second number:"))
operator=input("Enter operator (+,-,*,/):")

if operator == "+":
    result=add(num1,num2)

elif operator == "-":
    result=sub(num1,num2)

elif operator == "*":
    result=mul(num1,num2)

elif operator == "/":
    result=div(num1,num2)

else:
    result="Invalid Operator"

print("Result:",result)


