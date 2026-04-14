#Write a program to enter age of 50 students and create a histogram to display age as group of 0-10, 11-20, 21-30, 31-40, 41-50, 51-60, 60-120

import matplotlib.pyplot as plt

ages = [12,15,18,20,22,25,27,30,35,40,45,50,55,60,65,70,
        14,19,23,28,32,37,42,47,52,57,62,67,72,10,
        11,13,16,21,24,29,33,38,43,48,53,58,63,68,73,9,8,7,6,5]

bins = [0, 10, 20, 30, 40, 50, 60, 120]


plt.hist(ages, bins=bins)

plt.xlabel("Age Groups")
plt.ylabel("Number of Students")
plt.title("Age Distribution of Students")

plt.show()
