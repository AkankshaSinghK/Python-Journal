""" Write a Python program to Access the elements of a Series in Pandas from CSV file.
Also access the element from different position. """


import pandas as pd

df = pd.read_csv('new_students.csv')

print(df.iloc[0])
print(df.iloc[:3])

print(df.iloc[-1])
