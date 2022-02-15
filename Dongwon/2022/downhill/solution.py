# 1520

from collections import deque

m,n = 4,5
board=[
    [50,45,37,32,30]
    ,[35,50,40,20,25]
    ,[30,30,25,17,28]
    ,[27,24,22,15,10]
]
# board = [[-1] * n for _ in range(m)]


import sys
sys.stdin.readline
# m,n = map(int, input().split())
# board=[]
# for _ in range(m):
    # board.append(list(map(int, input().split())))
    
visited = [[-1] * n for _ in range(m)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x,y):
    if x == m-1 and y == n-1:
        return 1
    if visited[x][y] == -1:
        visited[x][y] = 0
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if -1 < nx < m and -1 < ny < n:
                if board[nx][ny] < board[x][y]:
                    visited[x][y] += dfs(nx,ny)
    print(visited)
    return visited[x][y]

print(dfs(0,0))
