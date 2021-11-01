from collections import deque

while True:
    w,h = map(int, input().split())
    
    if w == 0 and h == 0:
        break

    graph = [list(map(int, input().split())) for _ in range(h)]

    visited = [[False] * (w) for _ in range(h)]

    result = 0

    dx = [-1,1,0,0, -1,1,-1,1]
    dy = [0,0,-1,1, -1,-1,1,1]

    queue = deque([])

    def bfs(x,y):
        queue.append([x,y])
        while queue:
            a,b = queue.popleft()
            for i in range(8):
                nx = dx[i] + a
                ny = dy[i] + b
                if -1 < nx < h and -1 < ny < w:
                    if graph[nx][ny] == 1 and visited[nx][ny] == False:
                        visited[nx][ny] = True
                        queue.append([nx, ny])


    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1 and visited[i][j] == False:
                visited[i][j] = True
                bfs(i,j)
                result += 1

    print(result)