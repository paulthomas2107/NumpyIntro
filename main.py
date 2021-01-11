import numpy as np

# 1D Int
a = np.array([1, 2, 3, 5, 6, 7, 8, 9, 10])
print(a)

# 2D Float
b = np.array([[9.0, 8.0, 7.0], [12.1, 14.2, 9.2]])
print(b)

# Get array type
print(a.ndim)
print(b.ndim)

# Get shape
print(a.shape)
print(b.shape)

# Get Type
print(a.dtype)
print(b.dtype)

# Get Size
print(a.itemsize)
print(b.itemsize)
print(a.nbytes)
print(b.nbytes)

# Getting / Changing array values
a = np.array([[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14]])
print(a)
print(a[1, 5])   # 13
print(a[0, 3])   # 4
print(a[0, -3])  # 5

# Get a row
print(a[0, :])
print(a[1, :])
print(a[:, 2])

# Steps
print(a[0, 1:6:2])

# Changing item
a[1, 5] = 200
print(a)

# 3d example
b = np.array([[[1, 2], [3, 4], [5, 6], [7, 8]]])
print(b)
print(b[0, 1, 1])

# initialize arrays
a = np.zeros(10)
print(a)
a = np.zeros((2, 3))
print(a)
a = np.ones((2, 3))
print(a)
a = np.zeros((10, 9), dtype='int64')
print(a)
a = np.full((10, 10), 217)
print(a)

# Random
a = np.random.rand(4, 2)
print(a)
a = np.random.randint(10, size=(10, 10))
print(a)

# ID matrix
a = np.identity(10)
print(a)

# Repeats
arr = np.array([1, 2, 3, 4, 5, 6])
r1 = np.repeat(arr, 10)
print(r1)
arr = np.array([[1, 2, 3]])
r1 = np.repeat(arr, 3, axis=0)
print(r1)