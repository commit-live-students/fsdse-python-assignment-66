import numpy as np

def solution(array):
    """
    Enter code here
    """
    mat1 = np.absolute(np.identity(5) - np.ones([5,5]))
    mat1[0][0] = 1.0
    mat1[-1][-1] = 1.0
    return mat1

print(solution(5))
