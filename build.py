import numpy as np
def solution(arr):
    """
    Enter code here
    """
    shape = list(np.shape(arr))
    a = shape[0]
    b = shape[1]
    for i in range(1,a):
        arr[i,1:b-1] = 0
    print arr
    return arr
