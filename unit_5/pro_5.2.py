#Write a program to display all the records of student table (make use of fetchall() method).

import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="your_database"
)

cursor = conn.cursor()
cursor.execute("SELECT * FROM student")

for row in cursor.fetchall():
    print(row)

conn.close()
