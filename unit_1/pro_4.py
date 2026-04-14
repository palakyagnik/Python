#Write a program to enter 10 numbers and display all armstrong numbers from those numbers.

print("Enter 10 numbers:")
numbers = []

for i in range(10):
    num = int(input())
    numbers.append(num)

print("Armstrong numbers are:")

for num in numbers:
    temp = num
    sum = 0
    digits = len(str(num))

    while temp > 0:
        digit = temp % 10
        sum += digit ** digits
        temp //= 10

    if sum == num:
        print(num)
