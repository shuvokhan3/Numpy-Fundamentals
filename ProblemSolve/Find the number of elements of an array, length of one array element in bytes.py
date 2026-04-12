import numpy as np

def cal(arr):

    size = arr.size
    itemsize = arr.itemsize
    space = arr.nbytes

    return size, itemsize, space

arr = np.array([1, 2, 3, 4, 5])

size, itemsize, space = cal(arr)
print(f"Size: {size},\n Item Size: {itemsize},\n Space: {space}")
