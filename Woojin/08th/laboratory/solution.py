# --- 백준 스타일 ---

from collections import deque
from copy import deepcopy
from itertools import combinations

def install_walls(lab, indices):
    for i, j in indices:
        lab[i][j] = 1
    
    return lab

def count_spreaded_viruses(N, M, lab):
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    queue = deque()
    cnt = 0 # cnt: count virus
    
    for i in range(N):
        for j in range(M):
            if lab[i][j] == 2:
                queue.append((i, j))
    
    while queue:
        x, y = queue.popleft()
        
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            
            if not (0 <= nx < N and 0 <= ny < M):
                continue
            
            if lab[nx][ny] != 0:
                continue
            
            queue.append((nx, ny))
            lab[nx][ny] = 2
            cnt += 1
    
    return cnt

N, M = map(int, input().split())
lab = []
vacancies = []

for i in range(N):
    lab.append(list(map(int, input().split())))
    
    for j in range(M):
        if lab[i][j] == 0:
            vacancies.append((i, j))
        
vac_len = len(vacancies)
answer = 0

for indices in combinations(vacancies, 3):
    lab_copy = deepcopy(lab)
    lab_copy = install_walls(lab_copy, indices)
    answer = max(answer, vac_len - count_spreaded_viruses(N, M, lab_copy) - 3)

print(answer)