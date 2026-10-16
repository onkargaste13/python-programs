import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 30, 25]

plt.scatter(x, y, color="red")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.title("Scatter Chart")
plt.show()