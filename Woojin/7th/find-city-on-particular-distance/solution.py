# --- 프로그래머스 스타일 ---

from collections import deque

def get_graph(n, roads):
    graph = [[] for _ in range(n)]
    
    for road in roads:
        graph[road[0] - 1].append(road[1] - 1)
    
    return graph

def solution(n, roads, k, x):
    queue = deque([x - 1])
    graph = get_graph(n, roads)
    distance = [-1] * n
    distance[x - 1] = 0
    
    while queue:
        city = queue.popleft()
        
        for next_city in graph[city]:
            if distance[next_city] == -1:
                distance[next_city] = distance[city] + 1
                queue.append(next_city)
    
    result = [i + 1 for i, d in enumerate(distance) if d == k]
    
    if result:
        return result
    else:
        return [-1]

print(solution(4, [[1, 2], [1, 3], [2, 3], [2, 4]], 2, 1)) # [4]
print(solution(4, [[1, 2], [1, 3], [1, 4]], 2, 1)) # -1
print(solution(4, [[1, 2], [1, 3], [2, 3], [2, 4]], 1, 1)) # [2, 3]

# --- 백준 스타일 ---

from collections import deque

N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N)]

for _ in range(M):
    A, B = map(int, input().split())
    graph[A - 1].append(B - 1)

queue = deque([X - 1])
distance = [-1] * N
distance[X - 1] = 0
    
while queue:
    city = queue.popleft()

    for next_city in graph[city]:
        if distance[next_city] == -1:
            distance[next_city] = distance[city] + 1
            queue.append(next_city) 

exist_city = False

for i in range(N):
    if distance[i] == K:
        exist_city = True
        print(i + 1)

if not exist_city:
    print(-1)