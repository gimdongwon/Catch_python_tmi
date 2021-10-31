from collections import deque

computers = int(input())
lines = int(input())


graph = [[] for _ in range(computers+1)]
visited = [False for _ in range(computers+1)]

for _ in range(lines):
    x,y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x) # 양쪽에 안 넣어줘서 디버깅 오래 걸림

queue = deque([1])
visited[1] = True
while queue:
    start = queue.popleft()
    for v in graph[start]:
        if not visited[v]:
            visited[v] = True
            queue.append(v)

print(visited.count(True) - 1)