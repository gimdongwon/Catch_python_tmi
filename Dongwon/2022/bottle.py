from collections import deque

a,b,c = map(int, input().split())
visited = [[0] * (b+1) for _ in range(a+1)]
result = []

def pour(x,y):
    if not visited[x][y]:
        visited[x][y] = 1
        q.append((x,y))

def bfs():
    q.append((0,0))
    visited[0][0] = 1
    while q:
        x,y = q.popleft()
        z = c - x - y
        if x == 0:
            result.append(z)
        
        # a에서 b 물을 옮기는 경우
        if x > 0 and y < b:  # a에 물이 있고 b에 물이 가득차있지 않을 때
            w = min(x, b - y)
            pour(x - w, y + w)
        # a에서 c
        if x > 0 and z < c:
            w = min(x, c - z)
            pour(x - w, y)

        # b에서 a
        if y > 0 and x < a:
            w = min(y, a - x)
            pour(x + w, y - w)
        # b에서 c
        if y > 0 and z < c:
            w = min(y, c - z)
            pour(x, y - w)

        # c에서 a
        if z > 0 and x < a:
            w = min(z, a - x)
            pour(x + w, y)
        # c에서 b
        if z > 0 and y < b:
            w = min(z, b - y)
            pour(x, y + w)

q = deque([])
bfs()
result.sort()
print(' '.join(list(map(str, result))))