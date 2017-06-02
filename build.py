import numpy as np


def solution(array):
    new = np.zeros(array.shape)
    a, b = new.shape
    new[0,:] = 1
    new[:,0] = 1
    new[a-1, :] = 1
    new[:, b-1] = 1

    return new
