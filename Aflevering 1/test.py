import numpy as np
import matplotlib.pyplot as plt

def calcSeqVec(Vectors):
    Origins = np.concatenate((np.array([[0,0]]), Vectors[0:Vectors.shape[0]-1]))
    for i in range(1,Vectors.shape[0]):
        Vectors[i]=Vectors[i]+Vectors[i-1]
        Origins[i]=Origins[i]+Origins[i-1]
    return Origins, Vectors

def plotVectors(Vectors,Sequenced=True,Dots=True,Legend=[]):
    if Sequenced:
        Origins, Vectors = calcSeqVec(Vectors)
    for i in range(0,len(Vectors)):
        if Sequenced:
            xs = [Origins[i,0],Vectors[i,0]]
            ys = [Origins[i,1],Vectors[i,1]]
        else:
            xs = [0,Vectors[i,0]]
            ys = [0,Vectors[i,1]]
        if Dots:
            plt.plot(Origins[i,0],Origins[i,1],'ok')
            plt.plot(Vectors[i,0],Vectors[i,1],'ok')
        if Legend==[]:
            plt.plot(xs,ys)
        else:
            plt.plot(xs,ys,label=Legend[i])
    if Legend != []: plt.legend()


vectors = np.array([[3,8],[3,0.4],[0.7,-2.3],[-0.4,-1.5]])
label = ["OA","AB","BC","CP"]
plotVectors(vectors,Legend=label)

plt.axis('equal')
plt.xlim(-3,12) 
plt.ylim(-3,12) 
plt.grid(b=True, which='major')
plt.show()