m,n,k  = map(int, input().split())

dots = []

graph = [[0] * n for _ in range(m)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]
answer = []

for _ in range(k):
    x1,y1,x2,y2 = map(int, input().split())
    for x in range(y1, y2):
        for y in range(x1, x2):
            graph[x][y] = 1

for i in range(m):
    for j in range(n):
        if graph[i][j] == 0:
            result = 1
            graph[i][j] = 1
            queue = [[i,j]]
            while queue:
                x,y = queue[0][0], queue[0][1]
                del queue[0]
                for k in range(4):
                    nx = dx[k] + x
                    ny = dy[k] + y
                    if -1 < nx < m and -1 < ny <n and graph[nx][ny] == 0:
                        graph[nx][ny] = 1
                        result +=1
                        queue.append([nx,ny])
            answer.apspend(result)

print(len(answer))
answer.sort()
for item in answer:
    print(item, end=' ')