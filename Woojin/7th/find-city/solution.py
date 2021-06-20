from collections import deque

def get_graph(n, roads):
    graph = [[] for _ in range(n)]
    
    for road in roads:
        graph[road[0] - 1].append(road[1] - 1)
    
    return graph

def solution(n, roads, k, x):
    queue = deque([x - 1])
    graph = get_graph(n, roads)
    visited = [False] * n
    visited[x - 1] = True
    
    while queue:
        node = queue.popleft()
        result = []
        
        for next_node in graph[node]:
            if not visited[next_node]:
                visited[next_node] = True
                result.append(next_node)
        
        queue.extend(result)
        k -= 1
        
        if k == 0:
            if result:
                return sorted([x + 1 for x in result])
            else:
                return -1
    return -1

print(solution(4, [[1, 2], [1, 3], [2, 3], [2, 4]], 2, 1)) # [4]
print(solution(4, [[1, 2], [1, 3], [1, 4]], 2, 1)) # -1
print(solution(4, [[1, 2], [1, 3], [2, 3], [2, 4]], 1, 1)) # [2, 3]