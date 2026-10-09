import numpy as np

# 1. Create 1D Array
a = np.array([10, 20, 30, 40])
print("1D Array:")
print(a)

# 2. Create 2D Array
b = np.array([[1, 2], [3, 4]])
print("\n2D Array:")
print(b)

# 3. Create 3D Array
c = np.array([[[1, 2], [3, 4]],
              [[5, 6], [7, 8]]])
print("\n3D Array:")
print(c)

# 4. Addition
x = np.array([[10, 20], [30, 40]])
y = np.array([[2, 4], [5, 8]])

print("\nAddition:")
print(np.add(x, y))

# 5. Subtraction
print("\nSubtraction:")
print(np.subtract(x, y))

# 6. Multiplication
print("\nMultiplication:")
print(np.multiply(x, y))

# 7. Division
print("\nDivision:")
print(np.divide(x, y))

# 8. Transpose
print("\nTranspose:")
print(np.transpose(x))

# 9. Exponential
print("\nExponential:")
print(np.exp(b))

# 10. Add Character Labels
values = np.array([10, 20, 30, 40])
labels = ['A', 'B', 'C', 'D']

print("\nCharacter Labels:")
for label, value in zip(labels, values):
    print(label, ":", value)
