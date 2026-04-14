#Write a program to read above excel file and how many male and female students are there using bar graph.

import pandas as pd
import matplotlib.pyplot as plt

file = "pro_4.7"   
df = pd.read_excel(file)

df.columns = df.columns.str.strip().str.lower()

df['gender'] = df['gender'].astype(str).str.strip().str.lower()

gender_count = df['gender'].value_counts()


plt.bar(gender_count.index, gender_count.values)

plt.xlabel("Gender")
plt.ylabel("Number of Students")
plt.title("Male vs Female Students")

plt.show()
