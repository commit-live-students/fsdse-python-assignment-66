import numpy as np
def solution(array):
    """
    Enter code here
    """

    array = np.ones((5,5))
    array[1:4,1:4]=0
    return array
