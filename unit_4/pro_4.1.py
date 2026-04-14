# Write a program to load above excel file and display columns of file and data type of each column.

import pandas as pd

file = "data.xlsx"   
df = pd.read_excel(file)

print("Columns in the Excel file:")
print(df.columns)

print("\nData Types of each column:")
print(df.dtypes)
