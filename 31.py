""" Write a python program to save and load the array in binary and text files. """
import numpy as np

# create an array
arr = np.arange(1, 10)
print(arr)

# save the array in binary file
np.save('array.npy', arr)

# load the array from binary file
arr = np.load('array.npy')
print(arr)

# save the array in text file
np.savetxt('array.txt', arr, fmt='%d')

# load the array from text file
arr = np.loadtxt('array.txt', dtype=int)
print(arr)


