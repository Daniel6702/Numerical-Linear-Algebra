import numpy as np
import matplotlib.pyplot as plt

x = np.array([-0.5,0.0,1.0,2.0,3.0,4.0])
y = np.array([1.5,2,0.0,1.5,0.0,2.0])
fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.plot(x,y)
plt.show()