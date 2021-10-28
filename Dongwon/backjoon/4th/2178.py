from collections import deque
import sys

input = sys.stdin.readline

n,m = map(int, input().split())
graph = []

for _ in range(n):
    graph.append(list(map(int, list(input().strip()))))
visited = [[0] * m for _ in range(n)]

queue = deque([])
queue.append((0,0))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

while queue:
    x,y = queue.popleft()
    
    if x == n-1 and y == m-1:
        break
        
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if -1 < nx < n and -1 < ny < m and graph[nx][ny] == 1:
            if not visited[nx][ny]:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx,ny))

print(visited[n-1][m-1] + 1)