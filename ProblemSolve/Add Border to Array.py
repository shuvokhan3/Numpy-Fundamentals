import numpy as np

np_array = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
])

np_array_with_border = np.pad(np_array, pad_width=1, mode='constant', constant_values=8)
print(np_array_with_border)
