n = int(input())

lines = int(input())

graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]


for _ in range(lines):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(i):
    if visited[i] == False:
        visited[i] = True
        for j in graph[i]:
            if visited[j] == False:
                dfs(j)
    

dfs(1)

print(visited.count(True) - 1)