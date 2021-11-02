from collections import deque

n, m, v = map(int, input().split())

graph = [[] for _ in range(n+1)]
bfs_result = ""
dfs_result = ""
visited_bfs = [False for _ in range(n+1)]
visited_dfs = [False for _ in range(n+1)]

for __ in range(m):
    start, end = map(int,input().split())
    graph[start].append(end)
    graph[end].append(start)
    graph[start].sort()
    graph[end].sort()
print(graph)

# bfs

queue = deque([v])
visited_bfs[v] = True

while queue:
    q = queue.popleft()
    bfs_result += str(q) + " "
    for i in graph[q]:
        if not visited_bfs[i]:
            visited_bfs[i] = True
            queue.append(i)

def dfs(start):
    global dfs_result
    visited_dfs[start] = True
    dfs_result += str(start) + ' '
    for i in graph[start]:
        if not visited_dfs[i]:
            dfs(i)

dfs(v)

print(dfs_result)
print(bfs_result)