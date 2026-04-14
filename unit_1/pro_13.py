#Write a program to make use of map(), filter() and reduce() functions with context to lambda functions.

from functools import reduce


numbers = [1, 2, 3, 4, 5, 6]

squares = list(map(lambda x: x**2, numbers))
print("Squares using map():", squares)

evens = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers using filter():", evens)

total = reduce(lambda x, y: x + y, numbers)
print("Sum using reduce():", total)
