#Write a program to create function which shall accept any number of arguments and display total of all the numbers given as argument.

def find_total(*args):
    total = 0
    for num in args:
        total += num
    print("Total =", total)


find_total(60, 40, 70)
find_total(15, 45, 95, 35)
