import numpy as np

def solution(array):
    for i in range(1,4):
        for j in range(1,4):
            array[i][j] = 0.0
    return array





solution(np.ones((5,5)))
