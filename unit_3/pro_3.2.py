#Write a program to create a class for student with RollNo, Name, Age, Gender and methods named AddStudent() and DisplayStudent().

class Student:

    def AddStudent(self):
        self.rollno=int(input("Enter Roll Number:"))
        self.name=input("Enter Name:")
        self.age=int(input("Enter Age:"))
        self.gender=input("Enter Gender:")

    def DisplayStudent(self):
        print("\n--- Student Details ---")
        print("Roll Number:",self.rollno)
        print("Name:",self.name)
        print("Age:",self.age)
        print("Gender:",self.gender)

s1=Student()

s1.AddStudent()
s1.DisplayStudent()
