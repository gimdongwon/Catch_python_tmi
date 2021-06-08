# 스터디 용.
from collections import deque

def solution(N,K,apples, L, info):
    # 보드 생성
    board = [[0]*N for __ in range(N)]
    # 사과 배치
    for x,y in apples:
        board[x-1][y-1] = 1

    # 상 우 하 좌
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    # 방향 초기화('우' 로 시작)
    direction = 1
    # 현재 위치 초기화
    current_x, current_y = 0,0
    # 시간 초기화
    time = 1
    # 회전 방향, 초
    que = deque(info)
    rotate_time, rotate_direction = que.popleft()
    # 꼬리 모음
    visited = deque([[current_x,current_y]])
    # 2이면 현재 방문 중인 꼬리
    board[current_x][current_y] = 2
    while True:
        current_x += dx[direction]
        current_y += dy[direction]
        # 벽에 닿지 않고 꼬리가 아닌 경우에 탐색
        if -1 < current_x < N and -1 < current_y < N and board[current_x][current_y] != 2:
            # 방문하지 않앗을 때
            if board[current_x][current_y] != 1:
                # 한칸 움직여서 꼬리 축소
                temp_x, temp_y = visited.popleft()
                # print(temp_x, temp_y)
                board[temp_x][temp_y] = 0
            # 움직이기
            visited.append([current_x,current_y])
            # 꼬리 생성
            board[current_x][current_y] = 2
            # 회전하기
            if rotate_time == time:
                if rotate_direction == "D":
                    direction += 1
                    if direction > 3:
                        direction = 0
                else:
                    direction -= 1
                    if direction < 0:
                        direction = 3
                # 다음 회전각 탐색
                if que:
                    rotate_time, rotate_direction = que.popleft()
            time += 1
        else:
            break
        # print(time, [current_x, current_y], board)
    print(time, [current_x,current_y])
    return time
            
# solution(6,3,[(3,4),(2,5),(5,3)],3,[(3,"D"),(15,"L"),(17,"D")])
# solution(10,4,[(1,2),(1,3),(1,4),(1,5)],4,[(8,"D"),(10,"D"),(11,"D"),(13,"L")])
# solution(10,5,[(1,5),(1,3),(1,2),(1,6),(1,7)],4,[(8,"D"),(10,"D"),(11,"D"),(13,"L")])

# 백준 용

from collections import deque

N = int(input())
K = int(input())

board = [[0]*N for __ in range(N)]

apples = []
for __ in range(K):
    apples.append(list(map(int, input().split())))

L = int(input())

info = []
for __ in range(L):
    info.append(input().split())

for x,y in apples:
    board[x-1][y-1] = 1
    
dx = [-1,0,1,0]
dy = [0,1,0,-1]

direction = 1
current_x, current_y = 0,0
time = 1

que = deque(info)
visited = deque([[current_x, current_y]])

board[current_x][current_y] = 2
rotate_time, rotate_direction = que.popleft()

while True:
    current_x += dx[direction]
    current_y += dy[direction]
    if -1 < current_x < N and -1 < current_y < N and board[current_x][current_y] != 2:
        if board[current_x][current_y] != 1:
            temp_x, temp_y = visited.popleft()
            board[temp_x][temp_y] = 0
        visited.append([current_x,current_y])
        board[current_x][current_y] = 2
        if rotate_time == time:
            if rotate_direction == "D":
                direction += 1
                if direction > 3:
                    direction = 0
            else:
                direction -= 1
                if direction < 0:
                    direction = 3
            if que:
                rotate_time, rotate_direction = que.popleft()
        time += 1
    else:
        break
print(time)