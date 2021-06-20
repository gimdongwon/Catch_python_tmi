from copy import deepcopy
from math import isinf

def get_dist_matrix(weak):
    n = len(weak)
    matrix = [[0] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j] = weak[j] - weak[i]
    
    for i in range(n):
        for j in range(i):
            matrix[i][j] = 12 - matrix[j][i]

    return matrix

def get_n_friends(start, dist_matrix, dist):
    result = []
    dist.sort()
    
    dist_list = dist_matrix[start]
    reverse_dist_list = [(12 - d) % 12 for d in dist]

    max_dist = dist.pop()

    
    





def solution(n, weak, dist):
    dist_matrix = get_dist_matrix(weak)
    result = []

    for start in range(len(weak)):
        matrix_copy = deepcopy(dist_matrix)
        result.append(get_n_friends(start, matrix_copy, dist))
    
    if isinf(min(result)):
        return -1
    else:
        return min(result)