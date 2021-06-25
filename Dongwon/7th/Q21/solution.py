import sys
from collections import deque

input = sys.stdin.readline

N, L, R = map(int, input().split())

graph = []
# candinates = []
result = 0

for i in range(N):
    graph.append(list(map(int, input().split())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def checkGap(pos):
    global result
    # result += graph[pos[0]][pos[1]]
    visited = {(pos[0], pos[1])}
    q = deque()
    q.append(pos)
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # print(nx, ny, abs(graph[x][y] - graph[nx][ny]))
            if -1< nx < N and -1 < ny < N and L <= abs(graph[x][y] - graph[nx][ny]) <= R and (nx, ny) not in visited:
                q.append([nx,ny])
                visited.add((nx,ny))
                result += graph[nx][ny]
                union[nx][ny] = 1
    result //= len(visited)
    for item in visited:
        x,y = item
        graph[x][y] = result
    print(graph)
    return visited


total_count = 0
union = [[-1]*N for __ in range(N)]
idx = 0
print(union)
for i in range(N):
    for j in range(N):
        if union[i][j] == -1:
            checkGap([i,j])
    if i * j == N*N:
        break
    else:
        total_count += 1
print(total_count)