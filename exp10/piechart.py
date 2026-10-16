import matplotlib.pyplot as plt

sizes = [40, 30, 20, 10]

plt.pie(sizes, labels=["A", "B", "C", "D"],
        autopct="%1.1f%%")
plt.title("Pie Chart")
plt.show()