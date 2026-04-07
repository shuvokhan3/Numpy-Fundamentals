import numpy as np


# EXCERCISE 1: Create a NumPy array
def create_numpy_array():
    # Create and print a NumPy array 'a' containing the elements 1, 2, 3.
    a = np.array([1, 2, 3])
    print(a)

    # Create an array with 3 integers, starting from the default integer 0.
    b = np.arange(3)
    print(b)


    # Create an array that starts from the integer 1, ends at 20, incremented by 3.
    c = np.arange(1,20,3)
    print(c)

    #What if you wanted to create an array with five evenly spaced values in the interval from 0 to 100? As you may notice, you have 3 parameters that a function must take. One paremeter is the starting number, in this case 0, the final number 100 and the number of elements in the array, in this case, 5. NumPy has a function that allows you to do specifically this by using np.linspace().

    linspace_array = np.linspace(0, 100, 5,dtype=int)
    print(linspace_array)

    b_float = np.arange(3, dtype=float)
    print(b_float)

    char_arr = np.array(['Welcome to Math for ML!'])
    print(char_arr)
    print(char_arr.dtype) # Prints the data type of the array

    #One of the advantages of using NumPy is that you can easily create arrays with built-in functions such as:

    #np.ones() - Returns a new array setting values to one.
    #np.zeros() - Returns a new array setting values to zero.
    #np.empty() - Returns a new uninitialized array.
    #np.random.rand() - Returns a new array with values chosen at random.

    ## Return a new array of shape 3, filled with ones. 
    ones_array = np.ones(3, dtype=int)
    print(ones_array)

    ## Return a new array of shape 3, filled with zeroes.
    zeros_array = np.zeros(3, dtype=int)
    print(zeros_array)

    # Return a new array of shape 3, without initializing entries.
    empty_array = np.empty(3, dtype=int)
    print(empty_array)

    # Return a new array of shape 3 with random numbers between 0 and 1.
    random_array = np.random.rand(3)
    print(random_array)

create_numpy_array()







def convert_list_to_array():
    list = [1, 2, 3]

    # Convert the list to a NumPy array and print it.
    array = np.array(list)
    print(array)
    print(type(array))

convert_list_to_array()