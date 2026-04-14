#Write a program to display all the records of student table (make use of fetchone() method).

import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="your_database"
)

cursor = conn.cursor()

cursor.execute("SELECT * FROM student")

print("Student Records:\n")


row = cursor.fetchone()
while row is not None:
    print(row)
    row = cursor.fetchone()

conn.close()
