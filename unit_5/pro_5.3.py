#Write a program to search for particular student and display the details of student. If student is not found, related message shall be displayed

import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="your_database"
)

cursor = conn.cursor()

roll = int(input("Enter Roll Number to search: "))


query = "SELECT * FROM student WHERE rollno = %s"
cursor.execute(query, (roll,))

result = cursor.fetchone()


if result:
    print("Student Found:\n", result)
else:
    print("Student not found!")

conn.close()
