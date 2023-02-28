# NUMPY
import numpy as np

# Why Numpy?
a = [1, 2, 3, 4]
b = [2, 3, 4, 5]
ab = []

for i in range(0, len(a)):
    ab.append(a[i] * b[i])

a = np.array([1, 2, 3, 4])
b = np.array([2, 3, 4, 5])
a * b

# Creating Numpy Arrays
np.array([1, 2, 3, 4, 5])
type(np.array([1, 2, 3, 4, 5]))
np.zeros(10, dtype=int)
np.random.randint(0, 10, size=10)
np.random.normal(10, 4, (3, 4))

# Attributes of Numpy Arrays
a = np.random.randint(10, size=5)
print(a.ndim)
print(a.shape)
print(a.size)
print(a.dtype)

# Reshaping
np.random.randint(1, 10, size=9)
np.random.randint(1, 10, size=9).reshape(3, 3)
ar = np.random.randint(1, 10, size=9)
ar.reshape(3, 3)

# Index Selection
a = np.random.randint(10, size=10)
print(a[0])
print(a[0:5])
a[0] = 999

m = np.random.randint(10, size=(3, 5))
print(m[0, 0])
print(m[1, 1])
print(m[2, 3])

m[2, 3] = 999
m[2, 3] = 2.9

print(m[:, 0])
print(m[1, :])
print(m[0:2, 0:3])

# Fancy Index

v = np.arange(0, 30, 3)
print(v[1])
print(v[4])
catch = [1, 2, 3]
print(v[catch])

# Conditions on Numpy
v = np.array([1, 2, 3, 4, 5])

# With a classical loop
ab = []
for i in v:
    if i < 3:
        ab.append(i)

# With Numpy
print(v < 3)
print(v[v < 3])
print(v[v > 3])
print(v[v != 3])
print(v[v == 3])
print(v[v >= 3])

# Mathematical Operations

# Creating an array 'v'
v = np.array([1, 2, 3, 4, 5])

# Performing division operation on the array 'v' by 5
v / 5

# Performing mathematical operations on the array 'v'
v * 5 / 10
v ** 2
v - 1

# Using NumPy functions to perform subtract, add, mean, sum, min, max and variance on array 'v'
np.subtract(v, 1)
np.add(v, 1)
np.mean(v)
np.sum(v)
np.min(v)
np.max(v)
np.var(v)

# Updating array 'v' by subtracting 1
v = np.subtract(v, 1)

# Two Unknown Equation Solution with NumPy

# Coefficients of the equations
a = np.array([[5, 1], [1, 3]])
b = np.array([12, 10])

# Using NumPy's linalg.solve to solve the equation
np.linalg.solve(a, b)
