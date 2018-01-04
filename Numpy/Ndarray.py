import numpy as np

# Vector or 1-D tensor

a = np.array([1, 2, 3])

print(a)

# matrix or 2-D tensor

b = np.array([[1,2],[3, 4]])

print(b)

# minimum dimensions

c = np.array([1, 2, 3, 4, 5], ndmin = 2)

print(c)

# dtype parameter

d = np.array([1, 2, 3], dtype = complex)

print(d)
