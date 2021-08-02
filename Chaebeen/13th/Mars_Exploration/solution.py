# coding=utf-8
import heapq


def solution(n, route):
    INF = int(1e9)

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    # 그래프 구성
    graph = []
    for i in range(n):
        graph.append(route[i])

    distance = [[INF] * n for _ in range(n)]

    # 시작 위치 (0, 0), 비용 0
    q = [(graph[0][0], 0, 0)]
    distance[0][0] = graph[0][0]

    while q:
        dist, x, y = heapq.heappop(q)
        if distance[x][y] < dist:
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            cost = dist + graph[nx][ny]
            if cost < distance[nx][ny]:
                distance[nx][ny] = cost
                heapq.heappush(q, (cost, nx, ny))

    print(distance[n - 1][n - 1])


solution(3, [[5, 5, 4], [3, 9, 1], [3, 2, 7]])