# --- 백준 스타일 ---

from heapq import heappop, heappush

def dijkstra(graph):
    n = len(graph)
    INF = float("inf")
    cost = [[INF] * n for _ in range(n)]
    queue = []
    heappush(queue, (graph[0][0], 0, 0))
    cost[0][0] = graph[0][0]
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    while queue:
        c, x, y = heappop(queue)
        
        if (x, y) == (n - 1, n - 1):
            return c
        
        if cost[x][y] < c:
            continue
        
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            
            if not (0 <= nx < n and 0 <= ny < n):
                continue
            
            nc = c + graph[nx][ny]
            
            if cost[nx][ny] <= nc:
                continue
            
            cost[nx][ny] = nc
            heappush(queue, (nc, nx, ny))
    
T = int(input())
test_cases = []

for _ in range(T):
    N = int(input())
    test_case = []
    
    for _ in range(N):
        test_case.append(list(map(int, input().split())))
    
    test_cases.append(test_case)

for test_case in test_cases:
    print(dijkstra(test_case))