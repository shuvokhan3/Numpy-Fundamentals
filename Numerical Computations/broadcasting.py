import numpy as np

# 2D array (2 rows, 3 columns)
array_2d = np.array([[1, 2, 3],
                     [4, 5, 6]])

# 1D array (2 elements)
array_1d = np.array([100, 200])

# Reshape to (2, 1) for column broadcasting
array_column = array_1d.reshape((2, 1))

print("2D array shape:", array_2d.shape)      # (2, 3)
print("Reshaped array shape:", array_column.shape)  # (2, 1)

# Now broadcasting works column-wise
result = array_2d + array_column
print("Result:\n", result)