#Write a Python Program that creates a class and inherit into another class (Base Class : Student with rollno, name, gender, age) (Derived Class : Course with coursename, duration, fee)

class Student:
    def __init__(self, rollno, name, gender, age):
        self.rollno = rollno
        self.name = name
        self.gender = gender
        self.age = age

    def display_student(self):
        print("Roll No:", self.rollno)
        print("Name:", self.name)
        print("Gender:", self.gender)
        print("Age:", self.age)


# Derived Class
class Course(Student):
    def __init__(self, rollno, name, gender, age, coursename, duration, fee):
        # Calling base class constructor
        super().__init__(rollno, name, gender, age)
        self.coursename = coursename
        self.duration = duration
        self.fee = fee

    def display_course(self):
        print("Course Name:", self.coursename)
        print("Duration:", self.duration)
        print("Fee:", self.fee)


# Main Program
s = Course(101, "Palak", "Female", 20, "Python", "3 Months", 15000)

print("---- Student Details ----")
s.display_student()

print("\n---- Course Details ----")
s.display_course()
