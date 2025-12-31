import numpy as np

array_a = np.array([
    [101, 24],
    [102, 31]
])

array_b = np.array([
    [101, 24],
    [102, 31]
])

#this will concatenate value in the buttom  that is why the row is incresing
new_array = np.concatenate((array_a, array_b))
print(new_array)


#this will concatenate in axis 1 that is why row is not chages but coloum is chages
another_array = np.concatenate((array_a, array_b), axis=1)
print(another_array)

