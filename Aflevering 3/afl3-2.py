import numpy as np
from matplotlib import pyplot as plt

def y(x):
   return (-230/3)+(45/2)*x+(-5/6)*x**2

x = np.linspace(1, 13, 200)
plt.plot(x, y(x), color='red')

plt.show()