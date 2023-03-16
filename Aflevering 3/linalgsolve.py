import numpy as np
'''
a = np.array([[1,2,4],
              [1,5,25],
              [1,8,64]])

b = np.array([[35],
              [40],
              [50]])
'''
a = np.array([[1,8,64],
              [1,10,100],
              [1,11,121]])

b = np.array([[50],
              [65],
              [70]])

x = np.linalg.solve(a,b)

print(x)