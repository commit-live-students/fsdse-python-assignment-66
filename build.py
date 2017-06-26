import numpy as np

def solution(array):

    array = np.array(array)
    array[1:4,1:4] = 0

    return array
