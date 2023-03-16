import numpy as np
import matplotlib.pyplot as plt

#def y(x):
#   return (-230/3)+(45/2)*x+(-5/6)*x**2

a = np.array([[1,2,4,8,16],
              [1,5,25,125,625],
              [1,8,64,512,4096],
              [1,10,100,1000,10000],
              [1,11,121,1331,14641]])

b = np.array([[35],
              [40],
              [50],
              [65],
              [70]])

z = np.linalg.solve(a,b)

def y(x):
    return z[0]+z[1]*x+z[2]*x**2+z[3]*x**3+z[4]*x**4

x1 = np.linspace(1, 13, 200)
plt.plot(x1, y(x1), color='red')


x = [2.0,5.0,8.0,10.0,11.0]
y = [35.0,40.0,50.0,65.0,70.0]
plt.plot(x, y)

data = np.array([
    [8, 50],
    [10, 65],
    [11, 70],
    [2,35],
    [5,40]
])
x2, y2 = data.T
plt.scatter(x2,y2)

plt.xlabel('tid (min)')
plt.ylabel('temperatur (C)')
plt.xlim(1,13) 
plt.ylim(30,75) 
    
plt.show()