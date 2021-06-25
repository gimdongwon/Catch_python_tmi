from collections import deque
import copy

n,m = map(int, input().split(" "))

graph = []
answer = 0

for __ in range(n):
    graph.append(list(map(int, input().split(" "))))

viruses = deque()

dx = [-1,1,0,0]
dy = [0,0,-1,1]

# 벽을 3개 다 세운 뒤 바이러스 확산
def spread_viruses():
    global answer
    # 그래프는 일정해야되기 때문에 deepcopy 사용 => 개느려짐
    copy_graph = copy.deepcopy(graph)
    # 바이러스 감지
    for i in range(n):
        for j in range(m):
            if copy_graph[i][j] == 2:
                viruses.append([i,j])
    while viruses:
        x,y = viruses.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if -1 < nx < n and -1 < ny < m and copy_graph[nx][ny] == 0:
                copy_graph[nx][ny] = 2
                viruses.append([nx,ny])
    # 안전지역이 최대 일 때 answer 값을 변경
    cnt = 0
    for i in copy_graph:
        cnt += i.count(0)
    answer = max(answer, cnt)

# 벽을 3개 세워야 됨.
def set_wall(wall):
    if wall == 3:
        spread_viruses()
        return
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                set_wall(wall + 1)
                graph[i][j] = 0
set_wall(0)
print(answer)
