import numpy as np

def append(arr, values, axis=None):
    """
    Append values to the end of an array.

    Parameters:
    arr (array-like): The array to which values are appended.
    values (array-like): The values to append to the end of arr. It must be of the same shape as arr, except along the specified axis.
    axis (int, optional): The axis along which values are appended. If None, arr and values are flattened before use.

    Returns:
    ndarray: A new array containing arr followed by values.
    """
    return np.append(arr, values, axis=axis)

# Example usage:
if __name__ == "__main__":
    arr1 = np.array([1, 2, 3])
    arr2 = np.array([4, 5, 6])
    result = append(arr1, arr2)
    print(result)  # Output: [1 2 3 4 5 6]