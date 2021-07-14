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

# --- 백준 스타일 -> 런타임 에러(UnboundLocalError) ---

from collections import deque

def get_next_dir(current_dir, change_dir):
    if change_dir == "L":
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
    sec, change_dir = input().split()
    infos.append([int(sec), change_dir])

x, y = 1, 1 # x: 행, y: 열 / 머리 위치
dirs = {"R": (0, 1), "L": (0, -1), "D": (1, 0), "U": (-1, 0)}
current_dir = "R"
obstacles = deque() # 뱀의 몸통의 위치를 원소로 가지는 배열
total_sec = 0
stop = False

for sec, change_dir in infos:
    sec -= total_sec
    
    while sec:
        total_sec += 1
        
        for d, (dx, dy) in dirs.items():
            if current_dir == d:
                nx, ny = x + dx, y + dy

        obstacles.appendleft([x, y])

        if not (1 <= nx <= N and 1 <= ny <= N):
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
        
    current_dir = get_next_dir(current_dir, change_dir)

if stop:
    print(total_sec)
else:
    while 1 <= nx <= N and 1 <= ny <= N:
        total_sec += 1
        
        for d, (dx, dy) in dirs.items():
            if current_dir == d:
                nx, ny = x + dx, y + dy
                    
        obstacles.appendleft([x, y])
                
        if [nx, ny] in obstacles:
            break
        
        if [nx, ny] in apples:
            apples.remove([nx, ny])
        else:
            obstacles.pop()
        
        x, y = nx, ny
            
    print(total_sec)
    

# --- 답 수정 ---

from collections import deque

def get_next_dir(current_dir, change_dir):
    if change_dir == "L":
        next_dir = (current_dir-1) % 4
    else:
        next_dir = (current_dir+1) % 4
    
    return next_dir

def snake():
    current_dir = 1 # 초기 방향
    end_time = 1    # 게임이 끝나는 시간
    x, y = 0, 0     # 초기 뱀 위치
    visited = deque([(x, y)])  # 방문 위치
    board[x][y] = 2 # 뱀이 지나갔던 곳은 2로 저장
    
    while True:
        x, y = x + dx[current_dir], y + dy[current_dir]

        if not (0 <= x < N and 0 <= y < N and board[x][y] != 2): # 몸 또는 벽에 부딪힌 경우
            return end_time
        
        if board[x][y] != 1: # 사과가 없는 경우
            temp_x, temp_y = visited.popleft()
            board[temp_x][temp_y] = 0 # 꼬리 제거
        
        board[x][y] = 2
        visited.append((x, y))
            
        if end_time in time_dict.keys():
            current_dir = get_next_dir(current_dir, time_dict[end_time])
        
        end_time += 1

N = int(input())
K = int(input())
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1] # (dx[i], dy[i]): 상(i=0), 우(i=1), 하(i=2), 좌(i=3)
board = [[0] * N for _ in range(N)]

for _ in range(K):
    i, j = map(int, input().split())
    board[i - 1][j - 1] = 1  # board 위에 사과 위치 1로 저장

L = int(input())
time_dict = dict()

for _ in range(L):
    time, change_dir = input().split()
    time_dict[int(time)] = change_dir

print(snake())

# --- 아래 풀이가 왜 정답이 아닌지 고민하기 ---

from collections import deque

def get_next_dir(current_dir, change_dir):
    if change_dir == "L":
        next_dir = (current_dir-1) % 4
    else:
        next_dir = (current_dir+1) % 4
    
    return next_dir

def get_end_time():
    current_dir = 1 # 초기 방향
    end_time = 1    # 게임이 끝나는 시간
    x, y = 0, 0     # 초기 뱀 위치
    snake = deque([(x, y)]) # 방문 위치
    
    while True:
        x, y = x + dx[current_dir], y + dy[current_dir]

        if not (0 <= x < N and 0 <= y < N and (x, y) not in snake): # 몸 또는 벽에 부딪힌 경우
            return end_time
        
        if (x, y) not in apples: # 사과가 없는 경우
            snake.popleft() # 꼬리 제거
        else:
            apples.remove((x, y))
        
        snake.append((x, y)) # 머리 추가
            
        if end_time in change_dict.keys():
            current_dir = get_next_dir(current_dir, change_dict[end_time])
        
        end_time += 1

N = int(input())
K = int(input())
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1] # (dx[i], dy[i]): 상(i=0), 우(i=1), 하(i=2), 좌(i=3)
apples = []

for _ in range(K):
    apples.append(list(map(int, input().split())))

L = int(input())
change_dict = dict()

for _ in range(L):
    time, change_dir = input().split()
    change_dict[int(time)] = change_dir

print(get_end_time())