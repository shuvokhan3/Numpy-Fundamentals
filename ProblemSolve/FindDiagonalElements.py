import numpy as np

array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])


def diagonal_elements(arr):
    #extract all the diagonal elements
    final_val = np.diag(arr)
    return final_val

print(diagonal_elements(array))