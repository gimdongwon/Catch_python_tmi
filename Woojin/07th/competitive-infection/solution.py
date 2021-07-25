# --- 프로그래머스 스타일 ---

from collections import deque

def solution(N, test_tube, result_info):
    start = []
    
    for i in range(N):
        for j in range(N):
            if test_tube[i][j] != 0:
                start.append((test_tube[i][j], i, j))
                
    second, X, Y = result_info
    queue = deque([sorted(start)])
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while queue:
        if second == 0:
            return test_tube[X - 1][Y - 1]

        new_viruses = []
        viruses = queue.popleft()

        for virus in viruses:
            v_type, x, y = virus

            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                
                if not (0 <= nx < N and 0 <= ny < N):
                    continue
                
                if test_tube[nx][ny] == 0:
                    test_tube[nx][ny] = v_type
                else:
                    continue
                    
                new_viruses.append((v_type, nx, ny))
        
        if new_viruses:
            queue.append(sorted(new_viruses))
            second -= 1
        else:
            return test_tube[X - 1][Y - 1]

print(solution(3, [[1, 0, 2], [0, 0, 0], [3, 0, 0]], [2, 3, 2])) # 3
print(solution(3, [[1, 0, 2], [0, 0, 0], [3, 0, 0]], [1, 2, 2])) # 0
print(solution(4, [[1, 2, 3, 4], [0, 0, 0, 0], [0, 0, 0, 0], [1, 2, 3, 4]], [2, 2, 2])) # 2
print(solution(4, [[1, 0, 2, 0], [0, 0, 0, 0], [3, 0, 4, 0], [0, 0, 0, 0]], [1, 2, 2])) # 0
print(solution(4, [[1, 0, 2, 0], [0, 0, 0, 0], [3, 0, 4, 0], [0, 0, 0, 0]], [2, 2, 2])) # 1

# --- 백준 스타일 ---

from collections import deque

N, K = map(int, input().split())
test_tube = []
start = []

for i in range(N):
    test_tube.append(list(map(int, input().split())))
    
    for j in range(N):
        if test_tube[i][j] != 0:
            start.append((test_tube[i][j], i, j))

second, X, Y = map(int, input().split())
queue = deque([sorted(start)])
dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

while queue:
    if second == 0:
        break
    
    new_viruses = []
    viruses = queue.popleft()

    for virus in viruses:
        v_type, x, y = virus

        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            
            if not (0 <= nx < N and 0 <= ny < N):
                continue
            
            if test_tube[nx][ny] == 0:
                test_tube[nx][ny] = v_type
            else:
                continue
                
            new_viruses.append((v_type, nx, ny))
    
    queue.append(sorted(new_viruses))
    second -= 1
        
print(test_tube[X - 1][Y - 1])

# --- 모범 답안 ---

from collections import deque

N, K = map(int, input().split())
test_tube = []
start = []

for i in range(N):
    test_tube.append(list(map(int, input().split())))
    
    for j in range(N):
        if test_tube[i][j] != 0:
            start.append((test_tube[i][j], 0, i, j)) # (v_type, second, x, y)

queue = deque(sorted(start))
dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
second, X, Y = map(int, input().split())

while queue:
    v_type, s, x, y = queue.popleft()
    
    if second == s:
        break

    for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        
        if not (0 <= nx < N and 0 <= ny < N):
            continue
        
        if test_tube[nx][ny] == 0:
            test_tube[nx][ny] = v_type
        else:
            continue
                
        queue.append((v_type, s + 1, nx, ny))
        
print(test_tube[X - 1][Y - 1])