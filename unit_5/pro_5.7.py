#Write a program to display only those records who have valid email address as their information. Use regular expression here.

import mysql.connector
import re

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="your_database"
)

cursor = conn.cursor()

cursor.execute("SELECT * FROM student")
rows = cursor.fetchall()

pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

print("Students with Valid Email:\n")

for row in rows:
    email = str(row[4])   

    if re.match(pattern, email):
        print(row)

conn.close()
