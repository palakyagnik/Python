#Write a program to copy a text file using file handling mechanism.

source = open("pro_1.py", "r")
destination = open("pro_2.py", "w")

data = source.read()
destination.write(data)

source.close()
destination.close()

print("File copied successfully.")



