from copy import deepcopy

def get_rotated(matrix):

    return [list(reversed(m)) for m in zip(*matrix)]

def get_expanded(key, lock):
    M = len(key)
    N = len(lock)
    size = 2 * (M-1) + N
    expanded = [[0] * size for _ in range(size)]
    
    for x in range(N):
        for y in range(N):
            expanded[M - 1 + x][M - 1 + y] = lock[x][y]
    
    return expanded

def is_unlock(key, expanded_lock, i, j):
    M = len(key)
    N = len(expanded_lock) - 2 * (M-1)
    lock_copy = deepcopy(expanded_lock)
    
    for x in range(M):
        for y in range(M):
            lock_copy[i + x][j + y] += key[x][y]
    
    for x in range(N):
        for y in range(N):
            if lock_copy[M - 1 + x][M - 1 + y] != 1:
                return False
    
    return True

def solution(key, lock):
    M = len(key)
    N = len(lock)
    expanded_lock = get_expanded(key, lock)
    
    for _ in range(4):
        for i in range(M - 1 + N):
            for j in range(M - 1 + N):
                if is_unlock(key, expanded_lock, i, j):
                    return True
            
        expanded_lock = get_rotated(expanded_lock)
        
    return False