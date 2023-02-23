import numpy as np
from matplotlib import pyplot as plt

plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

def y(x):
   return 8*np.cos(x)-3*np.sin(7*x) #

n = 100

v = np.full([1, n], 1/2, dtype = float)[0]
v1 = np.full([1, n], 1/4, dtype = float)[0]
A = np.add(np.add(np.add(np.add(np.diag(v,0),np.diag(v[:-1],1)),np.diag(v[:-1],- 1)),np.diag(v1[:-2],- 2)),np.diag(v1[:-2],2))
#v = np.full([1, n], 1/2, dtype = float)[0]
#A = np.add(np.add(np.diag(v,0),np.diag(v[:-1],1)),np.diag(v[:-1],- 1)) #Ligger 3 matricer sammen, hver med en diagonal linje af værdier forskudt

rng = np.random.default_rng()
støj = rng.standard_normal(n)
x = np.linspace(-0, 9, n)
plt.plot(x, A@(y(x)+støj), color='red')



print(A)

plt.show()