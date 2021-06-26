from collections import deque
from copy import deepcopy

def bfs(n, l, r, population, visited):
    check_group = False
    
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                queue = deque([(i, j)]) # 초기화
                visited[i][j] = True
                dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                union = [(i, j, population[i][j])]
    
                while queue:    
                    x, y = queue.popleft()
                    
                    for dx, dy in dirs:
                        nx, ny = x + dx, y + dy
                        
                        if not (0 <= nx < n and 0 <= ny < n):
                            continue
                                                
                        if visited[nx][ny]:
                            continue
                        
                        if not l <= abs(population[nx][ny] - population[x][y]) <= r:
                            continue
                            
                        visited[nx][ny] = True
                        queue.append((nx, ny))
                        union.append((nx, ny, population[nx][ny]))
                
                if len(union) >= 2:
                    check_group = True
                    popn_mean = sum(r[2] for r in union) // len(union)
                    
                    for x, y, _ in union:
                        population[x][y] = popn_mean
    
    if check_group:
        return 1
    else:
        return 0

def solution(n, l, r, population):
    visited = [[False] * n for _ in range(n)]
    count = 0
    
    while True:
        visited_copy = deepcopy(visited)
        result = bfs(n, l, r, population, visited_copy)
        
        if result:
            count += result
        else:
            break
        
    return count

print(solution(2, 20, 50, [[50, 30], [20, 40]])) # 1
print(solution(2, 40, 50, [[50, 30], [20, 40]])) # 0
print(solution(2, 20, 50, [[50, 30], [30, 40]])) # 1
print(solution(3, 5, 10, [[10, 15, 20], [20, 30, 25], [40, 22, 10]])) # 2
print(solution(4, 10, 50, [[10, 100, 20, 90], [80, 100, 60, 70], [70, 20, 30, 40], [50, 20, 100, 10]])) # 3