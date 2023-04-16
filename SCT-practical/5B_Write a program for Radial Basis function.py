from scipy import *
from scipy.linalg import norm, pinv
from matplotlib import pyplot as plt
import numpy as np
import math
from pandas import *

class RBF:
    
    def __init__(self, indim, numCenters, outdim):
        self.indim = indim
        self.outdim = outdim
        self.numCenters = numCenters
        self.centers = [np.random.uniform(-1, 1, indim) for i in range(numCenters)]
        self.beta = 8
        self.W = np.random.random((self.numCenters, self.outdim))
        
    
    def _basisfunc(self, c, d):
        assert len(d) == self.indim
        return math.exp(-self.beta * norm(c-d)**2)
    
    
    def _calcAct(self, X):
        # calculate activations of RBFs
        G = np.zeros((X.shape[0], self.numCenters), float)
        
        for ci, c in enumerate(self.centers):
            for xi, x in enumerate(X):
                G[xi, ci] = self._basisfunc(c, x)
        return G
    
    
    def train(self, X, Y):
        # choose random center vectors from training set
        rnd_idx = np.random.permutation(X.shape[0])[:self.numCenters]
        self.centers = [X[i,:] for i in rnd_idx]
        
        print("center", self.centers)
        # calculate activations of RBFs 
        G = self._calcAct(X)
        print(G)
        
        #calulcate output weights(pseudoinverse)
        self.W = np.dot(pinv(G), Y)
        
    def test(self, X):
        G = self._calcAct(X)
        Y = np.dot(G, self.W)
        return Y
    
    
if __name__ =='__main__':
    # 1D Example
    n = 100
    x = np.mgrid[-1:1:complex(0,n)].reshape(n, 1)
    
    # set y and add random noise 
    y = np.sin(3 * (x+0.5)**3 - 1)
    
    # rbf regression
    rbf = RBF(1, 10, 1)
    rbf.train(x, y)
    z = rbf.test(x)
    
    # plot original data
    plt.figure(figsize=(12, 8))
    plt.plot(x, y, 'k-')
    
    # plot learning model
    plt.plot(rbf.centers, np.zeros(rbf.numCenters), 'gs')
    
    for c in rbf.centers:
        # RF prediction lines
        cx = np.arange(c-0.7, c+0.7, 0.01)
        cy = [rbf._basisfunc(array([cx_]), array([c])) for cx_ in cx]
        plt.plot(cx, cy, '-', color='gray', linewidth=0.2)
        
    plt.xlim()
    plt.show()
    
