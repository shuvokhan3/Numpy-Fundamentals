import numpy as np

array = np.array([[[1, 0], [3, 4]], [[np.nan, 6], [7, 8]]])
print(array.all())

print(np.isfinite(array))

new_array = np.identity(4)
print(new_array)
