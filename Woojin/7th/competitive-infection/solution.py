from collections import deque

def solution(n, test_tube, result_info):
    start = []
    
    for i in range(n):
        for j in range(n):
            if test_tube[i][j] != 0:
                start.append((test_tube[i][j], i, j))
                
    queue = deque([sorted(start)])
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    second, X, Y = result_info

    while queue:
        new_virus = []
        virus = queue.popleft()

        for v in virus:
            type, x, y = v

            for dx, dy in dirs:
                nx, ny = x + dx, y + dy

                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    continue
                
                if test_tube[nx][ny] == 0:
                    test_tube[nx][ny] = type
                else:
                    continue
                    
                new_virus.append((test_tube[nx][ny], nx, ny))
        
        if new_virus:
            queue.append(sorted(new_virus))
            second -= 1
        else:
            return test_tube[X - 1][Y - 1]
        
        if second == 0:
            return test_tube[X - 1][Y - 1]

    return test_tube[X - 1][Y - 1]

print(solution(3, [[1, 0, 2], [0, 0, 0], [3, 0, 0]], [2, 3, 2])) # 3
print(solution(3, [[1, 0, 2], [0, 0, 0], [3, 0, 0]], [1, 2, 2])) # 0
print(solution(4, [[1, 2, 3, 4], [0, 0, 0, 0], [0, 0, 0, 0], [1, 2, 3, 4]], [2, 2, 2])) # 2
print(solution(4, [[1, 0, 2, 0], [0, 0, 0, 0], [3, 0, 4, 0], [0, 0, 0, 0]], [1, 2, 2])) # 0
print(solution(4, [[1, 0, 2, 0], [0, 0, 0, 0], [3, 0, 4, 0], [0, 0, 0, 0]], [2, 2, 2])) # 1