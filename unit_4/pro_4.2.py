'''#Write a program to load above excel file and display following information- List of students from Rajkot City
- List of Male students
- List of Male students from Rajkot City
- List of students whose age >= 20'''

import pandas as pd

file = "data.xlsx"   
df = pd.read_excel(file)

print("Original Data:\n", df)

rajkot_students = df[df['City'] == 'Rajkot']
print("\nStudents from Rajkot City:\n", rajkot_students)

male_students = df[df['Gender'] == 'Male']
print("\nMale Students:\n", male_students)

male_rajkot = df[(df['Gender'] == 'Male') & (df['City'] == 'Rajkot')]
print("\nMale Students from Rajkot City:\n", male_rajkot)

age_students = df[df['Age'] >= 20]
print("\nStudents with Age >= 20:\n", age_students)

