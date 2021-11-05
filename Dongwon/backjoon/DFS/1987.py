import sys
input = sys.stdin.readline

r,c = map(int, input().split())

graph = [list(map(lambda x: ord(x)-65, input().rstrip())) for _ in range(r)]
visited = [0] * 26

dx = [-1,1,0,0]
dy = [0,0,-1,1]

result= 1
visited[graph[0][0]] = 1

def dfs(x,y, ans):
    global result
    result = max(ans, result)

    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if -1 < nx < r and -1 < ny < c and visited[graph[nx][ny]] == 0:
            visited[graph[nx][ny]] = 1
            dfs(nx, ny, ans+1)
            visited[graph[nx][ny]] = 0

dfs(0,0, result)

print(result)