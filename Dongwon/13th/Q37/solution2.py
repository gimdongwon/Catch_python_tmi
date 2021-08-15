# 플로이드를 다익스트라로

import pprint
import heapq

n, m = map(int, input().split())
INF = int(1e9)

distance = [[INF] * (n+1) for _ in range(n+1)]
graph = [[] for _ in range(n+1)]

for _ in range(m):
    start, end, cost = map(int, input().split())
    graph[start].append((cost, end))

for i in range(1, n+1):
    q = []
    heapq.heappush(q, (0, i))
    while q:
        current_cost, end = heapq.heappop(q)
        if current_cost < distance[i][end]:
            distance[i][end] = current_cost
            for cost, node in graph[end]:
                end_cost = current_cost + cost
                heapq.heappush(q, (end_cost,  node))

pprint.pprint(distance)

