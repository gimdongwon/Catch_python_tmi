from collections import deque

t = int(input())

for _ in range(t):
    m,n,k = map(int, input().split())

    graph = [[0] * m for _ in range(n)]

    for _ in range(k):
        y,x = map(int, input().split())
        graph[x][y] = 1

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    queue = deque([])

    def bfs(k):
        while queue:
            x,y = queue.popleft()
            graph[x][y] = k
            for l in range(4):
                nx = dx[l] + x
                ny = dy[l] + y
                if -1 < nx < n and -1 < ny < m:
                    if graph[nx][ny] == 1:
                        graph[nx][ny] = k
                        queue.append([nx,ny])
    cnt = 0
    k = 2
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                queue.append([i,j])
                bfs(k)
                cnt += 1
                k += 1

    print(cnt)
