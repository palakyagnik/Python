#Write a program to read a file and display its contents. At the end it shall also display no. of words available in file.

filename = "sample.txt"


with open(filename, "r") as file:
    content = file.read()       
    
    print("File Contents:\n")
    print(content)              
    
    words = content.split()     
    word_count = len(words)     
    
    print("\nTotal number of words in the file:", word_count)
