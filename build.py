import numpy as np

def solution(array):

    array = np.array(array)
    array[1:-1,1:-1] = 0

    return array
