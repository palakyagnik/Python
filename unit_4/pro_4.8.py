#Write a program to enter course and no. of students in each course. Display information using pie graph. The course with maximum students shall be displayed separately as a separate slice of pie graph.

import matplotlib.pyplot as plt

courses = []
students = []

for i in range(5):
    c = input("Enter course name: ")
    s = int(input("Enter number of students: "))
    courses.append(c)
    students.append(s)

max_index = students.index(max(students))

explode = [0] * len(courses)
explode[max_index] = 0.2   


plt.pie(students, labels=courses, explode=explode, autopct='%1.1f%%')

plt.title("Students in Each Course")

plt.show()
