import numpy as np
def solution(array):
    """
    Enter code here
    """
    array = np.ones((5,5))
    array[1][1:4]=array[2][1:4]=array[3][1:4]=0
    return array
