from collections import deque

n = int(input())

graph = [list(input()) for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

trans_graph = []

# 적록 색약의 그래프
for i in range(len(graph)):
    temp = []
    for j in range(len(graph[i])):
        if graph[i][j] == 'G':
            temp.append('R')
        else:
            temp.append(graph[i][j])
    trans_graph.append(temp)


result = 0
trans_result = 0
visited = [[False] * n for _ in range(n)]
trans_visited = [[False] * n for _ in range(n)]

def bfs(i,j, color, visited, graph):
    queue = deque([])
    queue.append([i,j])
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if -1 < nx < n and -1 < ny < n and visited[nx][ny] == False and color == graph[nx][ny]:
                queue.append([nx,ny])
                visited[nx][ny] = True
    return visited

for i in range(len(graph)):
    for j in range(len(graph[i])):
        if visited[i][j] == False:
            visited[i][j] = True
            visited = bfs(i,j, graph[i][j], visited, graph)
            result += 1
        if trans_visited[i][j] == False:
            trans_visited[i][j] = True
            trans_visited = bfs(i,j,trans_graph[i][j], trans_visited, trans_graph)
            trans_result += 1

print(result, trans_result)
