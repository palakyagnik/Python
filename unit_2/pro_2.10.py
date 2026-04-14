#Write a program to zip and unzip particular files.

import zipfile

# Creating a zip file
with zipfile.ZipFile('myfiles.zip', 'w') as z:
    z.write('file1.txt')
    z.write('file2.txt')

print("Files zipped successfully!")
