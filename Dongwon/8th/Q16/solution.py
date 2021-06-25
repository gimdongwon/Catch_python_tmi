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

def spread_viruses():
    global answer
    copy_graph = copy.deepcopy(graph)
    for i in range(n):
        for j in range(m):
            if copy_graph[i][j] == 2:
                viruses.append([i,j])
    while viruses:
        x,y = viruses.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if -1 < nx < n and -1 < ny < m:
                if copy_graph[nx][ny] == 0:
                    copy_graph[nx][ny] = 2
                    viruses.append([nx,ny])
    cnt = 0
    for i in copy_graph:
        cnt += i.count(0)
    answer = max(answer, cnt)

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
