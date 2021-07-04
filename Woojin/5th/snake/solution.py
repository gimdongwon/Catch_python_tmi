"""
머리가 장애물에 부딪히면 게임이 끝나는 로직
장애물 = 벽(인덱스 0 미만, N 초과) + 머리를 제외한 뱀의 몸통 
"""

# --- 프로그래머스 스타일 ---

from collections import deque

def get_changed_dir(current_dir, dir):
    if dir == "L":
        if current_dir == "R":
            changed_dir = "U"
        elif current_dir == "L":
            changed_dir = "D"
        elif current_dir == "U":
            changed_dir = "L"
        else:
            current_dir = "R"
    else:
        if current_dir == "R":
            changed_dir = "D"
        elif current_dir == "L":
            changed_dir = "U"
        elif current_dir == "U":
            changed_dir = "R"
        else:
            changed_dir = "L"
    
    return changed_dir

def solution(N, apples, infos):
    x, y = 1, 1 # x: 행, y: 열 / 머리 위치
    current_dir = "R"
    obstacles = deque() # 뱀의 몸통의 위치를 원소로 가지는 배열
    total_sec = 0
    
    for sec, dir in infos:
        sec -= total_sec
        
        while sec:
            total_sec += 1
            
            if current_dir == "R":
                nx, ny = x, y + 1
            elif current_dir == "L":
                nx, ny = x, y - 1
            elif current_dir == "U":
                nx, ny = x - 1, y
            else:
                nx, ny = x + 1, y
            
            obstacles.appendleft([x, y])

            if 1 <= nx <= N and 1 <= ny <= N:
                pass
            else:
                return total_sec
            
            if [nx, ny] in obstacles:
                return total_sec
            
            if [nx, ny] in apples:
                apples.remove([nx, ny])
            else:
                obstacles.pop()
            
            x, y = nx, ny
            sec -= 1
            
        current_dir = get_changed_dir(current_dir, dir)
    
    while 1 <= nx <= N and 1 <= ny <= N:
        total_sec += 1
        
        if current_dir == "R":
            nx, ny = x, y + 1
        elif current_dir == "L":
            nx, ny = x, y - 1
        elif current_dir == "U":
            nx, ny = x - 1, y
        else:
            nx, ny = x + 1, y
            
        obstacles.appendleft([x, y])
                
        if [nx, ny] in obstacles:
            return total_sec
        
        if [nx, ny] in apples:
            apples.remove([nx, ny])
        else:
            obstacles.pop()
        
        x, y = nx, ny
            
    return total_sec

print(solution(6, [[3, 4], [2, 5], [5, 3]], [[3, "D"], [15, "L"], [17, "D"]]))
print(solution(10, [[1, 2], [1, 3], [1, 4], [1, 5]], [[8, "D"], [10, "D"], [11, "D"], [13, "L"]]))
print(solution(10, [[1, 5], [1, 3], [1, 2], [1, 6], [1, 7]], [[8, "D"], [10, "D"], [11, "D"], [13, "L"]]))

# --- 백준 스타일 ---

from collections import deque

def get_next_dir(current_dir, dir):
    if dir == "L":
        if current_dir == "R":
            next_dir = "U"
        elif current_dir == "L":
            next_dir = "D"
        elif current_dir == "U":
            next_dir = "L"
        else:
            current_dir = "R"
    else:
        if current_dir == "R":
            next_dir = "D"
        elif current_dir == "L":
            next_dir = "U"
        elif current_dir == "U":
            next_dir = "R"
        else:
            next_dir = "L"
    
    return next_dir

N = int(input())
K = int(input())
apples = []
infos = []

for _ in range(K):
    apples.append(list(map(int, input().split())))
    
L = int(input())

for _ in range(L):
    sec, dir = input().split()
    infos.append([int(sec), dir])

x, y = 1, 1 # x: 행, y: 열 / 머리 위치
current_dir = "R"
obstacles = deque() # 뱀의 몸통의 위치를 원소로 가지는 배열
total_sec = 0
stop = False

for sec, dir in infos:
    sec -= total_sec
    
    while sec:
        total_sec += 1
        
        if current_dir == "R":
            nx, ny = x, y + 1
        elif current_dir == "L":
            nx, ny = x, y - 1
        elif current_dir == "U":
            nx, ny = x - 1, y
        else:
            nx, ny = x + 1, y
        
        obstacles.appendleft([x, y])

        if 1 <= nx <= N and 1 <= ny <= N:
            pass
        else:
            stop = True
            break
        
        if [nx, ny] in obstacles:
            stop = True
            break
        
        if [nx, ny] in apples:
            apples.remove([nx, ny])
        else:
            obstacles.pop()
        
        x, y = nx, ny
        sec -= 1
    
    if stop:
        break
        
    current_dir = get_next_dir(current_dir, dir)

if stop:
    print(total_sec)
else:
    while 1 <= nx <= N and 1 <= ny <= N:
        total_sec += 1
        
        if current_dir == "R":
            nx, ny = x, y + 1
        elif current_dir == "L":
            nx, ny = x, y - 1
        elif current_dir == "U":
            nx, ny = x - 1, y
        else:
            nx, ny = x + 1, y
            
        obstacles.appendleft([x, y])
                
        if [nx, ny] in obstacles:
            break
        
        if [nx, ny] in apples:
            apples.remove([nx, ny])
        else:
            obstacles.pop()
        
        x, y = nx, ny
            
    print(total_sec)