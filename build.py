import numpy as np

def solution(array):
    input_matrix = np.array(array)
    for num1 in range(1,4):
        for num2 in range(1,4):
            input_matrix[num1][num2] = 0
    return input_matrix
