# Write a program to delete the details of student in above table.

import mysql.connector


conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="your_database"
)

cursor = conn.cursor()


rollno = int(input("Enter Roll No to delete: "))


query = "DELETE FROM student WHERE rollno = %s"
cursor.execute(query, (rollno,))

conn.commit()

if cursor.rowcount > 0:
    print("Record deleted successfully!")
else:
    print("Student not found!")

conn.close()
