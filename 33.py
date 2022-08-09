""" Write a python program to create the Pandas Series from dictionary and also specify
the index. """

import pandas as pd


# dictionary of numbers in range 1 to 10
dictionary = {'a': 1, 'b': 2, 'c': 3, 'd': 4,
              'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10}
series = pd.Series(dictionary)
print(series)

# specify the index
series = pd.Series(dictionary, index=[
                   'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'])
print(series)
