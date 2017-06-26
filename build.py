import numpy as np
def solution(array):
    """
    Enter your code here
    """
    rows = array.shape[0]
    cols = array.shape[1]
    result = np.ones((rows,cols))
    result[1:rows-1,1:cols-1] = 0
    return result
