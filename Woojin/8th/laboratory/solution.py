# 백준 스타일

from collections import deque
from copy import deepcopy
from itertools import combinations

N, M = map(int, input().split(" "))
lab = []

for _ in range(N):
    lab.append(list(map(int, input().split(" "))))

def install_wall(lab, indices):
    for i, j in indices:
        lab[i][j] = 1
    
    return lab

def spread_virus(N, M, lab):
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    queue = deque()
    count = 0
    
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
            count += 1
    
    return count

def get_vacancies(N, M, lab):
    vacancies = []

    for i in range(N):
        for j in range(M):
            if lab[i][j] == 0:
                vacancies.append((i, j))
    
    return vacancies
          
vacancies = get_vacancies(N, M, lab)
vac_len = len(vacancies)
answer = 0

for indices in combinations(vacancies, 3):
    lab_copy = deepcopy(lab)
    lab_copy = install_wall(lab_copy, indices)
    answer = max(answer, vac_len - spread_virus(N, M, lab_copy) - 3)

print(answer)