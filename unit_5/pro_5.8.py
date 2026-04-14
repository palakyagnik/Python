#Write a program to load all the records from table and display only those details where names start with "N" and has length of 5 characters.

import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="your_database"
)

cursor = conn.cursor()

query = "SELECT * FROM student WHERE name LIKE 'N____'"
cursor.execute(query)

rows = cursor.fetchall()

print("Students with name starting with 'N' and length 5:\n")

for row in rows:
    print(row)

conn.close()
