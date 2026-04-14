#Write a program to read a file which contains only numbers. Display total of all numbers with maximum and minimum number.

file = open("numbers.txt", "r")

nums = []
for line in file:
    nums.append(int(line))

file.close()

print("Total =", sum(nums))
print("Maximum =", max(nums))
print("Minimum =", min(nums))
