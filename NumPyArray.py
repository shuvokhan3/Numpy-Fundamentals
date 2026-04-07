import numpy as np

# #Fundamentals of NumPy arrays including creation, indexing, slicing, and reshaping
#
# row_array = [20, 22, 25, 23, 18, 21, 24, 22, 19, 20, 23, 21]
#
# #create a numpy array
# array = np.array(row_array)
#
# #reshape this 1D array to 2D array
# new_array = array.reshape(3,4)
#
# val = new_array[1,2]
#
# print(new_array)
#
# print("Shape : ", new_array.shape)
#
# print("Postion value : ",val)


new_array = np.array([
    [1,2,3],
    [2,3,4],
    [4,5,6],
    [7,8,9]
])

print(new_array)

flatten_array = new_array.flatten()
print(flatten_array )
