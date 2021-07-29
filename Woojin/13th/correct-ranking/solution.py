# --- 백준 스타일 ---

N, M = map(int, input().split())
INF = float("inf")
cost = [[INF] * (N+1) for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    cost[a][b] = 1

for i in range(1, N + 1):
    cost[i][i] = 0

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if cost[i][j] != INF:
            cost[j][i] = cost[i][j]

answer = 0

for i in range(1, N + 1):
    if sum(cost[i][1:]) != INF:
    # if sum(1 for c in cost[i][1:] if c != INF) == N:
        answer += 1

print(answer)