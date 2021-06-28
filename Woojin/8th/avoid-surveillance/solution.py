# 백준 스타일

from copy import deepcopy
from itertools import combinations

def install_obs(corridor, indices): # obs: obstacle
    for i, j in indices:
        corridor[i][j] = "O"
    
    return corridor

def find_student(N, corridor, x, y): # (x, y): T의 위치
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        
        while (0 <= nx < N) and (0 <= ny < N):
            if corridor[nx][ny] == "O":
                break
            elif corridor[nx][ny] == "S":
                return True
            
            nx += dx
            ny += dy
    
    return False

def find_students(N, corridor):
    for i in range(N):
        for j in range(N):
            if corridor[i][j] == "T":
                if find_student(N, corridor, i, j):
                    return True
    
    return False

def get_vacancies(N, corridor):
    vacancies = []

    for i in range(N):
        for j in range(N):
            if corridor[i][j] == "X":
                vacancies.append((i, j))
    
    return vacancies

N = int(input())
corridor = []

for _ in range(N):
    corridor.append(list(input().split(" ")))

vacancies = get_vacancies(N, corridor)

for indices in combinations(vacancies, 3):
    corridor_copy = deepcopy(corridor)
    corridor_copy = install_obs(corridor_copy, indices)

    if not find_students(N, corridor_copy):
        print("YES")
        break
else:
    print("NO")