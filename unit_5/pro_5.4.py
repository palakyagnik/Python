#Write a program to insert the details of student in above table.

import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="your_database"
)

cursor = conn.cursor()


rollno = int(input("Enter Roll No: "))
name = input("Enter Name: ")
gender = input("Enter Gender: ")
age = int(input("Enter Age: "))
email = input("Enter Email: ")
mobile = input("Enter Mobile: ")
city = input("Enter City: ")


query = "INSERT INTO student (rollno, name, gender, age, email, mobile, city) VALUES (%s, %s, %s, %s, %s, %s, %s)"

values = (rollno, name, gender, age, email, mobile, city)

cursor.execute(query, values)

conn.commit()

print("Record inserted successfully!")

conn.close()
