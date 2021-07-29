# --- 백준 스타일 ---

from heapq import heappop, heappush

def dijkstra(graph):
    n = len(graph)
    INF = float("inf")
    cost = [INF] * n
    queue = []
    heappush(queue, (0, 1))
    cost[1] = 0
    
    while queue:
        c, now = heappop(queue)
        
        if cost[now] < c:
            continue
        
        for node in graph[now]:
            nc = c + 1
            
            if cost[node] <= nc:
                continue
            
            cost[node] = nc
            heappush(queue, (nc, node))
    
    return cost

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

cost = dijkstra(graph)
max_cost = max(cost[1:])
count = 0

for i in range(N + 1):
    if cost[i] == max_cost:
        first_max_idx = i
        break

for i in range(first_max_idx, N + 1):
    if cost[i] == max_cost:
        count += 1
        
print(first_max_idx, end=" ")
print(max_cost, end=" ")
print(count)
