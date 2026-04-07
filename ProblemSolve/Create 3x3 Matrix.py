import numpy as np

def create_3x3_matrix():
    #matrix
    matrix = np.array([[1,2,3],[5,6,7],[3,4,5]])
    return matrix

print(create_3x3_matrix())

#create_null_vector
def create_null_vector():
    null_value = np.zeros(10, dtype=int)
    return null_value
print(create_null_vector())


#create_null_vector
def create_null_vector():
    #create null vector
    null_value = np.zeros(10, dtype=int)
    

    #assign 1 to the 6th index of null vector
    for i in range(10):
        if(i == 5):
            null_value[i] = 1
    return null_value

#call the function
print(create_null_vector())
