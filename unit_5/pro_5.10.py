'''#Write a menu based program to perform following information.- Insert Student
- Update Student
- Search Student
- Delete Student
- List Students
- Exit'''

import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="your_database"
)

cursor = conn.cursor()

while True:
    print("\n--- Student Menu ---")
    print("1. Insert Student")
    print("2. Update Student")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. List Students")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    # 1. Insert
    if choice == 1:
        roll = int(input("Enter Roll No: "))
        name = input("Enter Name: ")
        gender = input("Enter Gender: ")
        age = int(input("Enter Age: "))
        email = input("Enter Email: ")
        mobile = input("Enter Mobile: ")
        city = input("Enter City: ")

        query = "INSERT INTO student VALUES (%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(query, (roll, name, gender, age, email, mobile, city))
        conn.commit()
        print("Student inserted successfully!")

    # 2. Update
    elif choice == 2:
        roll = int(input("Enter Roll No to update: "))
        city = input("Enter new City: ")
        mobile = input("Enter new Mobile: ")

        query = "UPDATE student SET city=%s, mobile=%s WHERE rollno=%s"
        cursor.execute(query, (city, mobile, roll))
        conn.commit()

        if cursor.rowcount > 0:
            print("Student updated successfully!")
        else:
            print("Student not found!")

    # 3. Search
    elif choice == 3:
        roll = int(input("Enter Roll No to search: "))
        query = "SELECT * FROM student WHERE rollno=%s"
        cursor.execute(query, (roll,))
        result = cursor.fetchone()

        if result:
            print(result)
        else:
            print("Student not found!")

    # 4. Delete
    elif choice == 4:
        roll = int(input("Enter Roll No to delete: "))
        query = "DELETE FROM student WHERE rollno=%s"
        cursor.execute(query, (roll,))
        conn.commit()

        if cursor.rowcount > 0:
            print("Student deleted successfully!")
        else:
            print("Student not found!")

    # 5. List
    elif choice == 5:
        cursor.execute("SELECT * FROM student")
        for row in cursor.fetchall():
            print(row)

    # 6. Exit
    elif choice == 6:
        print("Exiting program...")
        break

    else:
        print("Invalid choice!")

conn.close()
