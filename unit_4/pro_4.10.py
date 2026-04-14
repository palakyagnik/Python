#Write a program to read above file and use regular expression to display only those records who have mobile number with country code. For example, 91-9999933333 (2 digits of country code and 10 digits ofmobile)

import pandas as pd
import re

e
file = "pro_4.10"   
df = pd.read_excel(file)


df.columns = df.columns.str.strip().str.lower()

df['mobile'] = df['mobile'].astype(str).str.strip()

pattern = r'^\d{2}-\d{10}$'

valid_mobile = df[df['mobile'].apply(lambda x: re.match(pattern, x) is not None)]

print("Records with Valid Mobile Numbers (with country code):\n")
print(valid_mobile)
