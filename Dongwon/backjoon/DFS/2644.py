n = int(input())

parent, child = map(int, input().split())
visited = [0 for _ in range(n+1)]
result = 0

m = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
def dfs(x):
    for i in graph[x]:
        if visited[i] == 0:
            visited[i] = visited[x] + 1
            dfs(i)
        
dfs(parent)

print(visited[child] if visited[child] != 0 else -1)

