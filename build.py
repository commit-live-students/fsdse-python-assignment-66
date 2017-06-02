def solution(array):
    if array == None:
        return None

    for i in range(0,len(array)):
	    for j in range(0,len(array)):
		    if i == j:
			    if i == j == 1 or i == j == 2 or i == j == 3:
				    array[i][j] = 0
    return array
