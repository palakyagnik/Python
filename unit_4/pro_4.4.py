#Write a program to enter the profit of 5 years and display the profit as line graph.

import matplotlib.pyplot as plt

years = [1, 2, 3, 4, 5]
profits = [10000, 15000, 12000, 18000, 20000]

plt.plot(years, profits, marker='o')

plt.xlabel("Year")
plt.ylabel("Profit")
plt.title("Profit of 5 Years")

plt.show()
