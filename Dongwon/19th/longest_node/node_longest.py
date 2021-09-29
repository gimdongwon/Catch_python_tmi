# 1차 시도
import heapq

def solution(n, edge):
    INF = int(1e9)
    distance = [INF] * (n+1)
    distance[1] = 0
    heap = [[1,0]]
    
    while heap:
        current, current_cost = heapq.heappop(heap)
        for start, end in edge:
            cost = current_cost + 1
            if start == current and distance[end] > cost:
                distance[end] = cost
                heapq.heappush(heap, [end, cost])
            elif end == current and distance[start] > cost:
                distance[start] = cost
                heapq.heappush(heap, [start, cost])
        
    return distance[1:].count(max(distance[1:]))

# 2차 시도 정답

from collections import deque

def solution(n, edge):
    graph = [[] for _ in range(n+1)]
    for start, end in edge:
        graph[start].append(end)
        graph[end].append(start)
    
    visited = [0] * (n+1)
    que = deque([1])
    
    while que:
        current = que.popleft()

        for v in graph[current]:
            if visited[v] == 0:
                visited[v] = visited[current] + 1
                que.append(v)
                
    return visited[2:].count(max(visited)) 