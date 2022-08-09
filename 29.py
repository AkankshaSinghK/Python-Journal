import numpy as np

num_sq = np.array([[i, i**2] for i in range(5)])
print(num_sq)

num_zero = np.zeros((2, 2))
print(num_zero)

num_one = np.ones((2, 2))
print(num_one)

linsp = np.linspace(2, 3, 3)
print(linsp)

rand_arr = np.random.rand(2, 2)
print(rand_arr)

sum_num_sq = np.sum(num_sq)
print(sum_num_sq)
