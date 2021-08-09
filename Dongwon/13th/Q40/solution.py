import heapq
INF = int(1e9)

n, m = map(int, input().split())

start = 1

graph = [[] for _ in range(n+1)]

distance = [INF] * (n+1)

for _ in range(m):
    a,b = map(int, input().split())
    # 양쪽 통로, 길이는 1
    graph[a].append((b,1))
    graph[b].append((a,1))

q = []
heapq.heappush(q, (0, start))
distance[start] = 0

while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
        continue
    for item in graph[now]:
        cost = dist + item[1]
        if cost < distance[item[0]]:
            distance[item[0]] = cost
            heapq.heappush(q, (cost, item[0]))

distance[0] = 0 # 초기화 값 삭제
max_node_idx = distance.index(max(distance)) # 헛간 idx
max_node = max(distance) # 헛간까지의 거리 (최대 먼)
max_node_count = distance.count(max(distance)) # 같은 거리의 헛간 갯수

print(max_node_idx,max_node,max_node_count)