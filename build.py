def solution(array):
    """
    Enter code here
    """
    for i in range (0, len(array)):
        for j in range (0, len(array[i])):
            if (i == 0 and j == 0) or (i > 0 and j == 0) or (i == 0 and j > 0) or (i == len(array)-1) or (j == len(array)-1):
                array[i][j] = array[i][j]
            else:
                array[i][j] = 0

    return array

'''
import numpy as np

a = np.array([
    [1,1,1,1,1],
    [1,1,1,1,1],
    [1,1,1,1,1],
    [1,1,1,1,1],
    [1,1,1,1,1]
])

print solution(a)
'''
