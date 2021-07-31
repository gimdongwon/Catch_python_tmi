# --- 백준 스타일 ---
# 1. 각 간선의 비용이 1로 모두 같은 다익스트라 알고리즘 유형
# 2. 1번 헛간을 시작점으로 다익스트라 알고리즘을 적용 후
# 3. 각 헛간으로 갈 수 있는 비용(거리)이 최대인 헛간을 찾는 문제

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
