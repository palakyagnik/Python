#Write a program to display basic exception handling in python.

try:
    num1=int(input("Enter first number: "))
    num2=int(input("Enter second number:"))

    result = num1 / num2

    print("Result is:", result)

except ZeroDivisionError:
    print("Error: you cannot divide by zero!")

except ValueError:
    print("Error: Please enter valid integer numbers!")

except Exception as e:
        print("Unexpected Error:", e)

else:
    print("Division successful!")

finally:
    print("Program execution completed!")
