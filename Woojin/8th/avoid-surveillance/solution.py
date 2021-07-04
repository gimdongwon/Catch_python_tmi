# --- 백준 스타일 ---

from itertools import combinations

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

def find_students(N, corridor, teachers):
    for i, j in teachers:
        if find_student(N, corridor, i, j):
            return True
        
    return False
    
N = int(input())
corridor = []
teachers = []
vacancies = []

for i in range(N):
    corridor.append(list(input().split()))
    
    for j in range(N):
        if corridor[i][j] == "T":
            teachers.append((i, j))
        elif corridor[i][j] == "X":
            vacancies.append((i, j))

for indices in combinations(vacancies, 3):
    # 장애물 설치
    for i, j in indices:
        corridor[i][j] = "O"

    if not find_students(N, corridor, teachers):
        print("YES")
        break
    
    # 설치한 장애물 제거
    for i, j in indices:
        corridor[i][j] = "X"    
else:
    print("NO")