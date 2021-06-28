import numpy as np

array = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
# print(array)
# print(array.shape)

# matrix = np.zeros((3, 4), dtype=int)
# print(matrix)

# ones = np.ones((3, 4), dtype=int)
# print(ones)


# fives = np.full((4, 5), 5, dtype=int)
# print(fives)


# rands = np.random.random((4, 5))
# print(rands)

# print(rands > 0.2)

# print(rands[rands > 0.2])

print(array + array)


dimensions_inc = np.array([1, 2, 3])
dimensions_cm = dimensions_inc * 2.54
print(dimensions_cm)
