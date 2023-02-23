import numpy as np

#Same num of columns in a, as rows in b
a = np.array([[1,2,3],
              [5,6,7]])

b = np.array([[1,2,3,4],
              [5,6,7,8],
              [9,10,11,12]])

c = a@b

print(c)

x = np.array([[1,2],
              [5,6]])

y = np.array([[1,2],
              [5,6]])

print(x@y==y@x)
