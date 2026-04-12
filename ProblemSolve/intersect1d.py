import numpy as np

np_array = np.array([1, 2, 3, 4, 5])
np_array2 = np.array([3, 4, 5, 6, 7])

common_elements = np.intersect1d(np_array, np_array2)

print("Common elements between the two arrays:", common_elements)

