""" Write a python program using numpy to display array in the format as type of array,
dimension of array, shape of array , size of array, type of element of array and arange
the array. """

import numpy as np

# create an array
arr = np.arange(1, 10)

# display the array
print(arr)

# display the type of array
print(type(arr))

# display the dimension of array
print(arr.ndim)

# display the shape of array
print(arr.shape)

# display the size of array
print(arr.size)

# display the type of element of array
print(arr.dtype)

# display the arange of array
print(np.arange(1, 10))

