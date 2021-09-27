def solution(N, roads, K):
    town = [[500001] * (N + 1) for i in range(N + 1)]
    for i in range(N + 1) :
        town[i][i] = 0
    for road in roads :
        start, end, cost = road
        cost = min(town[start][end], cost)
        town[start][end] = cost
        town[end][start] = cost
    for k in range(1, N + 1) :
        for a in range(1, N + 1) :
            for b in range(1, N + 1) :
                town[a][b] = min(town[a][b], town[a][k] + town[k][b])
    return len([i for i in town[1] if i <= K])