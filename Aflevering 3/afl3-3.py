import numpy as np
import matplotlib.pyplot as plt
'''
def y(x):
   return (-230/3)+(45/2)*x+(-5/6)*x**2
'''

a5 = 100

a = np.array([[1,2,4,8,0,0,0,0],
              [1,5,25,125,0,0,0,0],
              [1,8,64,512,0,0,0,0],
              [0,1,4,12,0,0,0,0],
              [0,0,0,0,1,8,64,512],
              [0,0,0,0,1,10,100,1000],
              [0,0,0,0,1,11,121,1331],
              [0.1,1,16,192,0,-1,-16,-192]])


b = np.array([[35],
              [40],
              [50],
              [5/3],
              [50],
              [65],
              [70],
              [0]])

a1 = np.array([[1,2,4],
              [1,5,25],
              [1,8,64]])

b1 = np.array([[35],
              [40],
              [50]])
np.set_printoptions(suppress=True)

z = np.linalg.solve(a,b)
print(z)
z1 = np.linalg.solve(a1,b1)

def y(x):
    return z[0]+z[1]*x+z[2]*x**2+z[3]*x**3

def y1(x):
    return z[4]+z[5]*x+z[6]*x**2+z[7]*x**3

x1 = np.linspace(1, 8, 200)
plt.plot(x1, y(x1), color='red')

x2 = np.linspace(8, 13, 200)
plt.plot(x2, y1(x2), color='green')


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