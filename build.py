import numpy as np

def solution(n):
    """
    Enter code here
    """
    mat1 = np.absolute(np.identity(n) - np.ones([n,n]))
    mat1[0][0] = 1.0
    mat1[-1][-1] = 1.0
    return mat1

print(solution(5))
