#Write a program to make use of inner class.

class Student:
    
    def __init__(self, name):
        self.name = name
        self.laptop = self.Laptop()   

    def show(self):
        print("Student Name:", self.name)
        self.laptop.show()

   
    class Laptop:
        def __init__(self):
            self.brand = "HP"
            self.ram = "8GB"

        def show(self):
            print("Laptop Brand:", self.brand)
            print("RAM:", self.ram)



s1 = Student("Rahul")

s1.show()
