#Write a program to load above excel file and use dropna() and fillna() functions separately.

import pandas as pd


file = "pro_4.3"   
df = pd.read_excel(file)

df.columns = df.columns.str.strip().str.lower()

print("Original Data:\n", df)

drop_data = df.dropna()
print("\nData after dropna() (missing values removed):\n", drop_data)

fill_data = df.fillna({
    'name': 'Unknown',
    'age': 0,
    'gender': 'Not Specified',
    'city': 'Unknown'
})
print("\nData after fillna() (missing values filled):\n", fill_data)
