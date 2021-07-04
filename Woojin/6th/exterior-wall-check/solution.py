from copy import deepcopy
from math import isinf

def get_dist_matrix(n, weak):
    N = len(weak)
    matrix = [[0] * N for _ in range(N)]
    
    for i in range(N):
        for j in range(i + 1, N):
            matrix[i][j] = weak[j] - weak[i]
    
    for i in range(N):
        for j in range(i):
            matrix[i][j] = n - matrix[j][i]

    return matrix

def get_n_friends(start, dist_matrix, dist):
    result = []
    dist.sort()
    
    dist_list = dist_matrix[start]
    reverse_dist_list = [(12 - d) % 12 for d in dist]

    max_dist = dist.pop()


def solution(n, weak, dist):
    dist_matrix = get_dist_matrix(n, weak)
    result = []

    for start in range(len(weak)):
        matrix_copy = deepcopy(dist_matrix)
        result.append(get_n_friends(start, matrix_copy, dist))
    
    if isinf(min(result)):
        return -1
    else:
        return min(result)