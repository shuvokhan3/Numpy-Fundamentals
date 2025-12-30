import numpy as np

#indexing 1D array
array_val = np.array([1,2,3,4,5])
print("First Index Value is :", array_val[0])
print("Second Index Value is :", array_val[1])

#indexing 2D array
array_val2 = np.array([
    [1,2,3,4],
    [5,6,7,8]
])

print("2D array (0,1) value is : ", array_val2[0,1])

#slice 1D array
slice_val = array_val[1 : 5]
print("Sliced array is : ", slice_val)

#Slicing 2D array
array_2d = np.array([
    [1, 2, 3, 4, 5, 4, 5],
    [6, 7, 8, 9, 10, 9, 10],
    [11, 12, 1, 6, 9, 14, 15],
    [1, 2, 3, 4, 5, 4, 5],
    [6, 7, 8, 9, 7, 9, 10],
    [11, 12, 13, 14, 15, 14, 15]
])

#take every two row
print("Take every two row : ")
print(array_2d[::2])

#take every two coloum
print("Take every two coloum : ")
print(array_2d[ : , ::2])

print("slicing and with shape: ")
#So the slicing and with shape is
print(array_2d[::2 , ::2])


#Sorting by Row (Default)
final_val = np.sort(array_2d)
print("Array sort by row")
print(final_val)

print("Array sort by column")
sort_by_col = np.sort(array_2d, axis=0)
print(sort_by_col)


