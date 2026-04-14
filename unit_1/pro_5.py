#Write a program to enter 10 numbers and display largest odd number from the entered number.

largest_odd = 0
print("Enter 10 numbers:")

for i in range(10):
    num = int(input())
    if num % 2 != 0:
        
        if num > largest_odd:
            largest_odd = num

if largest_odd > 0:
    print("Largest odd number is:", largest_odd)
else:
    print("No odd numbers entered")
