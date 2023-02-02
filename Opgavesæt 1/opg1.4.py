import numpy as np
#a
a = 1.9
b = 1.3
c = 1.4
print( (a*(b+c)) - (a*b+a*c) )
print( (a*(b/c)) - ((a*b)/c) )
#b
x = np.finfo(np.float64).tiny
print("1.0 + a = "+str(1.0+x)+"       a: "+str(x))
#c
y = np.finfo(float).eps
print(1.0-y)
print(1.0-(1.0-y))
print(1.0-x)
print(1.0-(1.0-x))