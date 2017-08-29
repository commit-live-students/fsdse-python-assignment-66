import numpy as np
from copy import deepcopy

def solution(array):
    array = deepcopy(array)
    m, n = array.shape
    for i, row in enumerate(array[1 : m - 1]):
        row[1: m - 1].fill(0.)
    return array
