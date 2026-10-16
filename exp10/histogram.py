import matplotlib.pyplot as plt

marks = [20, 30, 40, 40, 50, 60, 60, 70, 80, 90]

plt.hist(marks, bins=5, color="blue", edgecolor="black")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.title("Histogram Chart")
plt.show()