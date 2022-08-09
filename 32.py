""" Write a python program to Create a Pandas Series from array. """
import numpy as np
import pandas as pd

# array of numbers in range 1 to 10
numbers = np.arange(1, 10)

series = pd.Series(numbers)
print(series)
