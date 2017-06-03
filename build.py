import numpy as np
def solution(array):
    """
    Enter code here
    """
    array = np.array(array)
    array[1:-1,1:-1] = 0

    return array
