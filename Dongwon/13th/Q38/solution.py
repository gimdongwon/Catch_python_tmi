INF = int(1e9)

N,M = map(int, input().split())

graph = [[INF] * (N+1) for _ in range(N+1)]

for a in range(N+1):
    for b in range(N+1):
        if a == b:
            graph[a][b] = 0

for _ in range(M):
    a,b = map(int, input().split())
    graph[a][b] = 1

for k in range(N+1):
    for a in range(N+1):
        for b in range(N+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

result = 0

for i in range(1, N+1):
    count = 0
    # 열마다 비교하여 도착할 수 있는 경우의 수가 존재하면 count += 1
    # 각 행이 전체를 거쳐 통과하는 위치를 확인하면 result += 1
    for j in range(1, N+1):
        if graph[i][j] != INF or graph[j][i]!=INF:
            count+=1
    if count == N:
        result += 1
print(result)