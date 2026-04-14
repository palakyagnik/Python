#Write a program to update the details of student in above table.

import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="your_database"
)

cursor = conn.cursor()


rollno = int(input("Enter Roll No to update: "))
new_city = input("Enter new City: ")
new_mobile = input("Enter new Mobile: ")


query = "UPDATE student SET city = %s, mobile = %s WHERE rollno = %s"
values = (new_city, new_mobile, rollno)

cursor.execute(query, values)

conn.commit()

if cursor.rowcount > 0:
    print("Record updated successfully!")
else:
    print("Student not found!")

conn.close()
