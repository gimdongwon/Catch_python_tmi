from collections import deque

n,m = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]

for _ in range(m):
    s,e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)


result = 0

def bfs(graph, start, visited):
    queue = deque()
    queue.append(start)
    visited[start] = True
    while queue:
        target = queue.popleft()
        for item in graph[target]:
            if visited[item] == False:
                queue.append(item)

for i in range(1, n+1):
    if visited[i] == False:
        bfs(graph, i, visited)
        result+=1
        
    
print(result)