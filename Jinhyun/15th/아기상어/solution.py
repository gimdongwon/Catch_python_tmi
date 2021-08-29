'''
아기 상어의 크기 : 2
자신과 같은 수의 물고기를 먹을 때 마다 1 증가
첫째 줄 : 공간 (n * n)
이후 줄 : 공간 상태
    0, 1, 2, 3, 4, 5, 6 -> 칸에 있는 물고기
    9 -> 아기 상어 위치

'''

from collections import deque
import heapq

def location(space) :
    len_space = len(space)
    for i in range(len_space) :
        for j in range(len_space) :
            if space[i][j] == 9 :
                space[i][j] = 0
                return space, i, j

def bfs(x, y, space, size) :
    q = deque()
    visited = set()
    visited.add((x, y))
    q.append((0, x, y))
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    space_size = len(space)
    eat = []
    while q :
        cnt, x, y = q.popleft()
        print(f"q : {q}")
        print(f"eat : {eat}")
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < space_size and ny >= 0 and ny < space_size and (nx, ny) not in visited :
                visited.add((nx, ny))
                if space[nx][ny] == 0 or space[nx][ny] == size :
                    q.append((cnt + 1, nx, ny))
                    continue
                if space[nx][ny] > size :
                    continue
                else :
                    heapq.heappush(eat, (cnt + 1, nx, ny))
    if eat :
        return eat[0]
    else :
        return None

def solution(n, space) :
    baby = 2
    cnt_size = 0
    result = 0
    space = list(map(int, space.split()))
    space = [space[i:i+n] for i in range(0, len(space), n)]
    # baby 위치
    space, baby_x, baby_y = location(space)
    while True :
        val = bfs(baby_x, baby_y, space, baby, cnt)
        print(f"val : {val}")
        if val is None :
            break
        cnt, x, y  = val
        result += cnt

        cnt_size += 1
        if baby == cnt_size :
            cnt_size = 0
            baby += 1
        baby_x, baby_y = x, y
        cnt = 0
    return result

# print(solution(3, '0 0 0 0 0 0 0 9 0'))
# print(solution(3, '0 0 1 0 0 0 0 9 0'))
print(solution(4, '4 3 2 1 0 0 0 0 0 0 9 0 1 2 3 4'))