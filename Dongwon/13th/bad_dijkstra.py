n,m = map(int, input().split())
INF = int(1e9)
start = int(input())

graph = [[] for _ in range(n+1)]

visited = [False] * (n+1)

distance = [int(1e9)] * (n+1)

# 모든 간선 정보
for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))

# 방문하지 않은 노드 중에서 가장 최단 거리가 짧은 노드의 번호를 반환

def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    distance[start] = 0
    visited[start] = True
    print(graph, distance, start, visited)
    # 해당 index의 거리를 재 생성해줌.
    for j in graph[start]:
        distance[j[0]] = j[1]
    # 시작 노드를 제외한 전체 n-1 개의 노드에 대한 반복
    for _ in range(n-1):
        # 현재 최단 거리가 가장 짧은 노드를 꺼내서, 방문 처리
        now = get_smallest_node()
        visited[now] = True
        # 현재 노드와 연결된 다른 노드를 확인
        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost

dijkstra(start)

print(distance)