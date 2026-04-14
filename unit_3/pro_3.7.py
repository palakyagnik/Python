#Use appropriate functions for each classWrite a program to display MRO using multiple inheritance. Multiple inheritance can be done as per your choice.

class Student:
    def __init__(self, name):
        self.name = name

    def show_student(self):
        print("Student Name:", self.name)


# Base Class 2
class Course:
    def __init__(self, coursename):
        self.coursename = coursename

    def show_course(self):
        print("Course Name:", self.coursename)


# Derived Class (Multiple Inheritance)
class Result(Student, Course):
    def __init__(self, name, coursename, marks):
        Student.__init__(self, name)
        Course.__init__(self, coursename)
        self.marks = marks

    def show_result(self):
        print("Marks:", self.marks)


# Main Program
r = Result("Palak", "Python", 85)

print("---- Details ----")
r.show_student()
r.show_course()
r.show_result()

# Display MRO
print("\nMethod Resolution Order (MRO):")
for cls in Result.__mro__:
    print(cls)
