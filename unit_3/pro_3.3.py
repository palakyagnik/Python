#Write a program to make use of class method and instance method.

class Student:
    school = " Tanna School"   
    def AddStudent(self, roll_no, name, age, gender):
        self.roll_no = roll_no
        self.name = name
        self.age = age
        self.gender = gender

    def DisplayStudent(self):
        print("Roll_no is:", self.roll_no)
        print("Name is:", self.name)
        print("Age is:", self.age)
        print("Gender is:", self.gender)
        print("School is:", Student.school)

    @classmethod
    def ChangeSchool(cls, new_name):
        cls.school = new_name


s1 = Student()

s1.AddStudent(1, "Palak", 20, "Female")
Student.ChangeSchool("Tanna School")
s1.DisplayStudent()

print()

