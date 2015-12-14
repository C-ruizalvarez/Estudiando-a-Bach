#!\usr\bin\python

import numpy as np
from intento2random import rn as rnd
import matplotlib.pyplot as plt

l = 1000

def aleatorios(n,l):
    dat = []
    i = 0
    
    for i in range(l):
        A = rnd(n)
        lista = list(A[:,0]) + list(A[:,1])

        dat.append(lista)

    np.savetxt('datos.dat', dat, fmt = '%d')

aleatorios(4,l)
    
def genhistograma(h):

    data = np.loadtxt('datos.dat')
    Hist = []
    
    for i in range(l):
        Hist.append(data[i][h])

    return Hist

def histograma(h,l):

    Hist = genhistograma(h)
    
    if h <= 3:
        x = np.arange(1.5,13,1)
        H = np.histogram(Hist, bins = [1,2,3,4,5,6,7,8,9,10,11,12,13])
        y = H[0]
        plt.hist(Hist, bins = [1,2,3,4,5,6,7,8,9,10,11,12,13])
        plt.grid(True)
        plt.xlim((1,13))
        plt.ylabel("frecuencia")
        plt.title("Histograma %d"%(h+1))
        plt.errorbar(x,y, yerr = np.sqrt(y), fmt = '.')
        plt.savefig("hist%d"%(h))
        plt.close()
        
    elif h > 3:
        x = np.arange(0.5,11,1)
        H = np.histogram(Hist, bins = [0,1,2,3,4,5,6,7,8,9,10,11])
        y = H[0]
        plt.hist(Hist, bins = [0,1,2,3,4,5,6,7,8,9,10,11])
        plt.grid(True)
        plt.xlim((0,11))
        plt.ylabel("frecuencia")
        plt.title("Histograma %d"%(h+1))
        plt.errorbar(x,y, yerr = np.sqrt(y), fmt = '.')
        plt.savefig("hist%d"%(h))
        plt.close()
        
for i in range(8):
    H = histograma(i,l)

