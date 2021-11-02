# # 1차 시도 bfs

# import copy
# from collections import deque
# n = int(input())

# graph = []

# max_num = 0

# for item in range(n):
#     target = list(map(int, input().split()))
#     max_num = max(max_num, max(target))
#     graph.append(target)

# dx = [-1,1,0,0]
# dy = [0,0,-1,1]

# queue = deque([])
# answer = 0

# def bfs(i,j, board, visited):
#     queue.append([i,j])
#     while queue:
#         x,y = queue.popleft()
#         for q in range(4):
#             nx = dx[q] + x
#             ny = dy[q] + y
#             if -1 < nx < n and -1 < ny < n:
#                 if board[nx][ny] != 0 and visited[nx][ny] == False:
#                     visited[nx][ny] = True
#                     queue.append([nx,ny])
#     return visited

# for k in range(1, max_num):
#     result = 0
#     board = copy.deepcopy(graph)
#     visited = [[False] * n for _ in range(n)]
#     for i in range(n):
#         for j in range(n):
#             if board[i][j] < k:
#                 board[i][j] = 0
    
#     for i in range(n):
#         for j in range(n):
#             if board[i][j] != 0 and visited[i][j] == False:
#                 visited = bfs(i,j, board, visited)
#                 result += 1
                
#     answer = max(answer, result)

# print(answer)




import  sys

input = sys.stdin.readline

sys.setrecursionlimit(100000)

dx = [-1,1,0,0]
dy = [0,0,-1,1]

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

answer = 0


def dfs(x,y,h):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if -1 < nx < n  and -1 < ny < n and graph[nx][ny] > h and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx,ny,h)

for k in range(max(map(max, graph))):
    visited = [[False] * n for _ in range(n)]
    result = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] > k and not visited[i][j]:
                result += 1
                visited[i][j] = True
                dfs(i,j,k)
    answer = max(answer, result)

print(answer)