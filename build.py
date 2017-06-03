import numpy as np
def solution(array):
    """
    Enter code here
    """
    shape = list(np.shape(array))
    multiplier = np.zeros(np.shape(array))

    multiplier[0,:] = 1
    multiplier[-1,:] = 1
    multiplier[:,0] = 1
    multiplier[:,-1] = 1
    return np.multiply(array, multiplier)
