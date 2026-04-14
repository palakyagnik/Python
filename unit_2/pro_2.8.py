#Write a program to read file which has marks entry of student and display details with total, percentage and grade (Consider a file which has comma separated data with RollNo, Student Name, Mark1, Mark2, Mark3 and Mark4).

file = open("pro_5.py", "r")

for line in file:
    data = line.strip().split(",")

    roll = data[0]
    name = data[1]
    m1 ,m2 ,m3 ,m4 = int(data[2]),int(data[3]),int(data[4]),int(data[5])

    total = m1 + m2 + m3 + m4
    per = total / 4

    if per >= 75:
        grade = "A"
    elif per >= 60:
        grade = "B"
    elif per >= 50:
        grade = "C"
    else:
        grade = "Fail"

    print(roll, name, "Total:", total, "Percentage:", per, "Grade:", grade)

file.close()
    

    
