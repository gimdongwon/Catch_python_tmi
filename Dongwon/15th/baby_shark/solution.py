# 아기상어

# bfs, 그래프 이론으로 푸는것같은데,, 생각보다 까다로운 듯하다. 여러개의 개념이 겹쳐서

from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

shark_x, shark_y = 0,0

# 상어 위치 확인
for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            shark_x, shark_y = i,j
            graph[i][j] = 0

def bfs(x,y):
    q, visited = deque([(x,y)]), set([(x,y)])
    time = 0
    shark = 2
    eat = 0
    eat_flag = False

    answer = 0
    while q:
        size = len(q)
        # 왼쪽 상어 우선시 하기 위한 sort
        q = deque(sorted(q))
        for _ in range(size):
            x,y = q.popleft()

            # 현재 위치에 아기 상어보다 작은 물고기가 있어서 먹은 경우
            if graph[x][y] != 0 and graph[x][y] < shark:
                graph[x][y] = 0
                eat += 1
                # 상어 사이즈 업
                if eat == shark:
                    shark += 1
                    eat = 0

                # 먹고 난 뒤, 현재 위치 기준으로 다시 탐색
                q, visited = deque(), set([(x,y)])
                eat_flag = True
                # 정답이 마지막으로 먹은 시간이기에 미리 저장
                answer = time

            for i in range(4):
                nx,ny = x + dx[i], y + dy[i]
                if -1 < nx < n and -1 < ny < n and (nx,ny) not in visited:
                    # 0도 넣음
                    if graph[nx][ny] <= shark:
                        q.append((nx,ny))
                        visited.add((nx, ny))
            # 해당 위치에서 먹은 후라면 추가 탐색이 필요없으므로 for 탈출
            if eat_flag:
                eat_flag = False
                break
        time += 1
    return answer

print(bfs(shark_x, shark_y))