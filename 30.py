""" Write a python program to create numpy array and use the functions as reshape ,
flattern and transpose """

import numpy as np

# create an array
arr = np.arange(1, 10)
print(arr)

# reshape the array
arr = arr.reshape(3, 3)
print(arr)

# transpose the array
print(arr.transpose())

# flattern the array
arr = arr.flatten()
print(arr)

