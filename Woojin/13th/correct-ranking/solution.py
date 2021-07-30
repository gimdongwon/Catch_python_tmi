# --- 백준 스타일 ---
# 1. 플로이드 워셜 알고리즘 사용
# 2. 모든 학생들을 대상으로 성적 비교 후
# 3. 성적을 비교한 행렬을 대칭행렬로 만들었음
# 4. 각 행에 INF가 없다면 성적 순위를 정확히 알 수 있는 학생인 것

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