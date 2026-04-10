import numpy as np

# array_a = np.array([
#     [101, 24],
#     [102, 31]
# ])
#
# array_b = np.array([
#     [101, 24],
#     [102, 31]
# ])
#
# #this will concatenate value in the buttom  that is why the row is incresing
# new_array = np.concatenate((array_a, array_b))
# print(new_array)
#
#
# #this will concatenate in axis 1 that is why row is not chages but coloum is chages
# another_array = np.concatenate((array_a, array_b), axis=1)
# print(another_array)


#Reshaping array

#Creating 1D array
array_1D = np.array([1,2,3])

#create 2D array
array_2D = np.array([[1,2,3],[4,5,6],[7,8,9]])

# #reshape 1D array
new_array = array_1D.reshape((3,1))
print(new_array)


#Concatenate
final_array = np.concatenate((array_2D, new_array), axis=1)
print(final_array)


