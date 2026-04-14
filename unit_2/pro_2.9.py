# Write a program to do student operations using menu as followsa) Add Student
#b) Search Student
#c) List All Students
#d) Update Student
#e) Delete Student
#f) Exit

students = []

while True:
    print("/n------ Student Menu -------")
    print("a) Add Student")
    print("b) Search Student")
    print("c) List All Student")
    print("d) Delete Student")
    print("e) Exit")

    choice = input("Enter your choice:")

    if choice == 'a':
        roll = input("Enter Roll No:")
        name = input("Enter Name:")
        marks = input("Enter Marks:")

        student = {"roll" : roll , "name" : name , "marks" : marks}
        student.append(student)
        print("Student added successfully.")

    elif choice == 'b':
        roll = input("Enter Roll No to search:")
        found = False
        for s in students:
            if s["roll"] == roll:
                print("Roll:", s["roll"])
                print("Name:", s["name"])
                print("Marks:", s["marks"])
                found = True

            if not found:
                print("Student not found.")

            elif choice == 'c':
                if len(students) == 0:
                    print("No student found.")

            else:
                print("\nStudent List:")
            for s in students:
                print(s["roll"], s["name"], s["marks"])

    elif choice == 'd':
        roll = input("Enter Roll No to update: ")
        for s in students:
            if s["roll"] == roll:
                s["name"] = input("Enter new name: ")
                s["marks"] = input("Enter new marks: ")
                print("Student updated.")
                break
        else:
            print("Student not found.")

    elif choice == 'e':
        roll = input("Enter Roll No to delete: ")
        for s in students:
            if s["roll"] == roll:
                students.remove(s)
                print("Student deleted.")
                break
        else:
            print("Student not found.")

    elif choice == 'f':
        print("Program exited.")
        break

    else:
        print("Invalid choice.")
                

