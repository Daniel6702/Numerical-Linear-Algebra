import numpy as np
import matplotlib.pyplot as plt

def calcSeqVec(Vectors):
    Origins = np.concatenate((np.array([[0,0]]), Vectors[0:Vectors.shape[0]-1]))
    for i in range(1,Vectors.shape[0]):
        Vectors[i]=Vectors[i]+Vectors[i-1]
        Origins[i]=Origins[i]+Origins[i-1]
    return Origins, Vectors

def plotVectors(Vectors,Sequenced=True,Dots=True,Legend=[]):
    vecs = []
    Origins = np.linspace((0,0),(0,0),Vectors.shape[0])
    if Sequenced: Origins, Vectors = calcSeqVec(Vectors)
    for i in range(0,len(Vectors)):
        xs = [Origins[i,0],Vectors[i,0]]
        ys = [Origins[i,1],Vectors[i,1]]
        if Dots: plt.plot(Vectors[i,0],Vectors[i,1],'ok')  
        if Legend==[]: vecs.append(plt.plot(xs,ys))
        else: vecs.append(plt.plot(xs,ys,label=Legend[i]))
    if Legend != []: plt.legend()
    return vecs

### A
#Vektorer 
a = np.array([3, 8])
b = np.array([3, 0.4])
c = np.array([0.7, -2.3])
d = np.array([-0.4,-1.5])

### B
sumOP = a+b+c+d # = [6.3, 4.6]
print(sumOP)

### C
theta = np.pi
rotation = np.array([[ np.cos(theta),  -np.sin(theta) ],
                     [ np.sin(theta),   np.cos(theta) ]])
b = rotation.dot(b) 
c = rotation.dot(c) 
d = rotation.dot(d) 


vectors = np.array([a,b,c,d])
label = ["OA","AB","BC","CP"]
plotVectors(vectors,Legend=label)

plt.axis('equal')
plt.xlim(-3,12) 
plt.ylim(-3,12) 
plt.grid(b=True, which='major')
plt.show()