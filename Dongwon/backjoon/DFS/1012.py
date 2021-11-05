import sys
sys.recursionlimit(100000)

T = int(input())
for _ in range(T):
    m,n,k = map(int, input().split())

    graph = [[0] * m for _ in range(n)]
    result = 0

    for _  in range(k):
        a,b = map(int, input().split())
        graph[b][a] = 1

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    def dfs(x,y):
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if -1 < nx < n and -1 < ny < m:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = 0
                    dfs(nx, ny)

    for i in range(n):
        for j in range(m):
            if graph[i][j] > 0:
                dfs(i,j)
                result += 1

    print(result)