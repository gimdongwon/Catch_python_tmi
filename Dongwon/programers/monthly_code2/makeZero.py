def solution(a, edges):
    if sum(a) != 0:
        return -1
    result = -1
    visited = [False] * len(a)
    for i in range(len(a)):
        while a[i]!= 0 and visited[i] == False:
            if a[i] > 0:
                a[i] -= 1
            else:
                a[i] += 1
            result += 1
        visited[i] = True
    return result


import sys
sys.setrecursionlimit(10 ** 6)

def solution(a, edges):
    if sum(a) != 0:
        return -1 
    result = 0
    board = [[] for _ in range(len(a))]
    visited = [False for _ in range(len(a))]
    
    for x,y in edges:
        board[x].append(y)
        board[y].append(x)
    
    
    def dfs(x):
        nonlocal result
        visited[x] = True
        for i in board[x]:
            if visited[i] == False:
                a[x] += dfs(i)
        result += abs(a[x])
        
        return a[x]
    
    dfs(0)
    return result