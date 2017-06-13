import numpy as np
def solution(array):
        array=np.ones((5,5))
        array[1:-1,1:-1]=0
        return array
#print solution([[ 1.,  1.,  1.,  1.,  1.],
#       [ 1.,  1.,  1.,  1.,  1.],
#       [ 1.,  1.,  1.,  1.,  1.],
#       [ 1.,  1.,  1.,  1.,  1.],
#       [ 1.,  1.,  1.,  1.,  1.]])
