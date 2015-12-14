#!\usr\bin\python

import numpy as np

def rn(n):
    A = np.zeros((n,2))

    for i in range(len(A)):
        A[i,0] = np.random.randint(1,13)
        A[i,1] = np.random.randint(0,11)

    return A


