""" Question: plot graph for equation
                1) y=2x^2+2x+10
                2) y=2x+5 
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2, 2, 100)
y = (2*(x**2)) + (2*x) + 10

a = np.linspace(-2, 2, 100)
b = (2*x)+5

fig = plt.figure(figsize=(10, 5))

# Create the plot
plt.plot(x, y)
plt.plot(a, b)

plt.grid(True)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Plot of y = (2x^2) + (2x) + 10')
plt.legend(['y = 2x^2+ 2x + 10', 'y = 2^x + 5'])

# Show the plot
plt.savefig('plot.png')
plt.show()
