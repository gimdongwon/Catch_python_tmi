from collections import deque

n,m = map(int, input().split())

graph = []

for _ in range(m):
    graph.append(list(map(int, input().split())))


dx = [-1,1,0,0]
dy = [0,0,-1,1]

queue = deque()

def bfs():
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if -1 < nx < m and -1 < ny < n:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = 1 + graph[x][y]
                    queue.append((nx,ny))


for i in range(m):
    for j in range(n):
        if graph[i][j] == 1:
            queue.append((i,j))
    
bfs()

res = 0
for i in graph:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    res = max(res, max(i))
print(res - 1)