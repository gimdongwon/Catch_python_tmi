from collections import deque

n = int(input())

graph = []

for _ in range(n):
    graph.append(list(map(int, list(input()))))

dx = [-1,1,0,0]
dy = [0,0,-1,1]


def bfs(graph, x,y):
    queue = deque()
    queue.append((x,y))
    graph[x][y] = 0
    cnt = 1
    while queue:
        i,j = queue.popleft()
        graph[i][j] = 0
        for k in range(4):
            nx = dx[k] + i
            ny = dy[k] + j
            if -1 < nx < n and -1 < ny < n and graph[nx][ny] == 1:
                queue.append((nx,ny))
                graph[nx][ny] = 0
                cnt += 1
    return cnt

result = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            result.append(bfs(graph, i,j))

result.sort()

print(len(result))

for item in result:
    print(item)