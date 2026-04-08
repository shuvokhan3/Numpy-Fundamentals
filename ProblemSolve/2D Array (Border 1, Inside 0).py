import numpy as np

#create a 2d array
array = np.array([[1,2,3,3],[4,5,6,3],[7,8,9,3],[2,3,5,7],[4,5,6,7]])
array[1:-1, 1:-1] = 0
print(array)


