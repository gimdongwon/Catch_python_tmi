n = int(input())

graph = [list(map(int, list(input()))) for _ in range(n)]

visited = [[False] * n for _ in range(n)]

cnt = 0
result = []

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x,y):
    visited[x][y] = True
    graph[x][y] = 0
    global cnt
    cnt += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if -1 < nx < n and -1 < ny < n and graph[nx][ny] == 1:
            dfs(nx,ny)

for i in range(n):
    for j in range(n):
        if visited[i][j] == False and graph[i][j] == 1:
            dfs(i,j)
            result.append(cnt)
            cnt = 0
print(len(result))
result.sort()
for item in result:
    print(item)