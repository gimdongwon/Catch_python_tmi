from collections import deque

n,k = map(int, input().split())

graph = [0] * 100001
queue = deque()
queue.append(n)

while queue:
    target = queue.popleft()
    if target == k:
        print(graph[target])
        break
    for nx in (target - 1, target + 1, target * 2):
        if -1 < nx < 100001 and graph[nx] == 0:
            graph[nx] = graph[target] + 1
            queue.append(nx)