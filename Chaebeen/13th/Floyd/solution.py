# coding=utf-8
def solution(n, m, bus):
    INF = int(1e9)
    graph = [[INF] * n for _ in range(n)]

    for i in range(m):
        a, b, c = bus[i]
        graph[a - 1][b - 1] = min(graph[a - 1][b - 1], c)

    # 시작 도시와 도착 도시가 같은 경우
    for i in range(n):
        graph[i][i] = 0

    # 플로이드 점화식
    for k in range(n):
        for i in range(n):
            for j in range(n):
                graph[i][j] = min(graph[i][k] + graph[k][j], graph[i][j])

    # 이동할 수 없는 경우
    for i in range(n):
        for j in range(n):
            if graph[i][j] == INF:
                graph[i][j] = 0

    for i in range(n):
        print(graph[i])


solution(5, 14, [[1, 2, 2], [1, 3, 3], [1, 4, 1], [1, 5, 10], [2, 4, 2],
                 [3, 4, 1], [3, 5, 1], [4, 5, 3], [3, 5, 10], [3, 1, 8],
                 [1, 4, 2], [5, 1, 7], [3, 4, 2], [5, 2, 4]])
