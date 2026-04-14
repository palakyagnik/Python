#Write a program to read above file and use regular expression in order to display records who has valid emails.

import pandas as pd
import re

file = "pro_4.9"   
df = pd.read_excel(file)

df.columns = df.columns.str.strip().str.lower()

df['email'] = df['email'].astype(str).str.strip()

pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

valid_emails = df[df['email'].apply(lambda x: re.match(pattern, x) is not None)]

print("Records with Valid Emails:\n")
print(valid_emails)
