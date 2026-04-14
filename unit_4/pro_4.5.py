# Write a program to enter the name of 5 companies and its employee size and display as bar graph.

import matplotlib.pyplot as plt

companies = ["TCS", "Infosys", "Wipro", "Google", "Amazon"]
employees = [500000, 300000, 250000, 150000, 200000]

plt.bar(companies, employees)

plt.xlabel("Companies")
plt.ylabel("Number of Employees")
plt.title("Employee Size of Companies")

plt.show()
