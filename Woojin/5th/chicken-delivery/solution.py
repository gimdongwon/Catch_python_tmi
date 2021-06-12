from copy import deepcopy
from itertools import combinations

def get_chicken_dist(i, j, matrix): # 최적화 하기 
    N = len(matrix)                 # 거리 1부터 시작하여 주어진 거리에 치킨 집이 있으면 바로 루프 중지하는 방법 사용하면 완전 탐색보다 빠르게 만들 수 있을 듯
    result = []
    
    for x in range(N):
        for y in range(N):
            if matrix[x][y] == 2:
                result.append(abs(i - x) + abs(j - y))
    
    return min(result)

def get_city_chicken_dist(matrix):
    N = len(matrix)
    result = 0
    
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 1:
              result += get_chicken_dist(i, j, matrix)
    
    return result

def get_rm_index(matrix, n):
    N = len(matrix)
    index_list = []
    
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 2:
                index_list.append((i, j))
    
    return combinations(index_list, n)

def solution(N, M, matrix):
    n_total_chicken = sum(1 for row in matrix for r in row if r == 2)
    n = n_total_chicken - M
    rm_index = get_rm_index(matrix, n)
    result = []
    
    for indices in rm_index:
        matrix_copy = deepcopy(matrix)
        
        for i, j in indices:
            matrix_copy[i][j] = 0
        
        result.append(get_city_chicken_dist(matrix_copy))
    
    return min(result)


print(solution(5, 3, [[0, 0, 1, 0, 0], [0, 0, 2, 0, 1], [0, 1, 2, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 2]])) # 5
print(solution(5, 2, [[0, 2, 0, 1, 0], [1, 0, 1, 0, 0], [0, 0, 0, 0, 0], [2, 0, 0, 1, 1], [2, 2, 0, 1, 2]])) # 10
print(solution(5, 1, [[1, 2, 0, 0, 0], [1, 2, 0, 0, 0], [1, 2, 0, 0, 0], [1, 2, 0, 0, 0], [1, 2, 0, 0, 0]])) # 11
print(solution(5, 1, [[1, 2, 0, 2, 1], [1, 2, 0, 2, 1], [1, 2, 0, 2, 1], [1, 2, 0, 2, 1], [1, 2, 0, 2, 1]])) # 32
