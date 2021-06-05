from collections import deque

def solution(N,K,apples, L, inpo):
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
    # 꼬리 모음
    
    que = deque(inpo)
    visited = deque([[current_x,current_y]])
    board[current_x][current_y] = 2
    rotate_time, rotate_direction = que.popleft()
    while True:
        current_x += dx[direction]
        current_y += dy[direction]
        if -1 < current_x < N and -1 < current_y < N and board[current_x][current_y] != 2:
            if board[current_x][current_y] != 1:
                temp_x, temp_y = visited.popleft()
                # print(temp_x, temp_y)
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
        # print(time, [current_x, current_y], board)
    print(time, [current_x,current_y])
    return time
            
solution(6,3,[(3,4),(2,5),(5,3)],3,[(3,"D"),(15,"L"),(17,"D")])
solution(10,4,[(1,2),(1,3),(1,4),(1,5)],4,[(8,"D"),(10,"D"),(11,"D"),(13,"L")])
solution(10,5,[(1,5),(1,3),(1,2),(1,6),(1,7)],4,[(8,"D"),(10,"D"),(11,"D"),(13,"L")])