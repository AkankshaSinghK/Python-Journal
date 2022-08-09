""" Write a python program to Create Pandas Series using NumPy functions (linspace,random,repeat,flattern) """

import numpy as np
import pandas as pd

lnsp = np.linspace(1, 10, 10)
print(lnsp)

rnd = np.random.rand(10)
print(rnd)

rpt = np.repeat(5, 10)
print(rpt)

rpt = rpt.reshape(2,5)
print(rpt)

rpt = rpt.flatten()

s_lnsp = pd.Series(lnsp)
print(s_lnsp)

s_rnd = pd.Series(rnd)
print(s_rnd)

s_rpt = pd.Series(rpt)
print(s_rpt)

