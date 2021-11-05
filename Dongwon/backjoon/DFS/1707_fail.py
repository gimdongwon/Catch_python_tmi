import sys
input = sys.stdin.readline

# t = int(input())

# for _ in range(t):
v,e = map(int, input().split())

graph = [[] for _ in range(v+1)]

for _ in range(e):
    x,y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(i, visited):
    for j in range(len(graph[i])):
        if visited[graph[i][j]] == False:
            visited[graph[i][j]] = True
            dfs(graph[i][j], visited)

flag = False
print(graph)
for i in range(1,v+1):
    visited = [False for _ in range(v+1)]
    origin = graph[i][:]
    graph[i] = []
    temp = []
    
    for idx, item in enumerate(graph):
        if i in item:
            item.remove(i)
            temp.append(idx)
    dfs(1, visited)
    
    for j in temp:
        graph[j].append(i)
    graph[i] = origin
    
    if True in visited and visited.count(True) % 2 == 0:
        flag = True
        break
print('YES' if flag else 'NO')