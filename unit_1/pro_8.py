'''#Write a Python program to perform following operation on given string input:
a) Count Number of Vowel in given string
b) Count Length of string (donot use len() )
c) Reverse string
d) Find and replace operation
e) check whether string entered is a palindrome or not'''

string = input("Enter a string: ")

# a) Count number of vowels
vowels = "aeiouAEIOU"
vowel_count = 0
for ch in string:
    if ch in vowels:
        vowel_count += 1
print("Number of vowels:", vowel_count)


# b) Count length of string (without using len())
length = 0
for ch in string:
    length += 1
print("Length of string:", length)


# c) Reverse string
reverse = ""
for ch in string:
    reverse = ch + reverse
print("Reversed string:", reverse)


# d) Find and replace operation
find_word = input("Enter word to find: ")
replace_word = input("Enter word to replace with: ")
new_string = string.replace(find_word, replace_word)
print("Updated string:", new_string)


# e) Check palindrome
if string == reverse:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")
