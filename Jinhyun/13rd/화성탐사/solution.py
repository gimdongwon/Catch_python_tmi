import heapq

def solution(n, data) :
    INF = int(1e9)
    distance = [[INF] * n for _ in range(n)]
    q = []
    heapq.heappush(q, (0, (0,0)))
    distance[0][0] = 0
    while q :
        dist, now = heapq.heappop(q)
        x, y = now
        if distance[x][y] < dist :
            continue
        udlr = [(x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)]
        for cord in udlr :
            a, b = cord
            if a < 0 or a > n - 1 or b < 0 or b > n - 1 :
                continue
            cost = dist + data[a][b]
            if cost < distance[a][b] :
                distance[a][b] = cost
                heapq.heappush(q, (cost, (a, b)))
    return distance[n-1][n-1] + data[0][0]

print(solution(3, [[5,5,4],[3,9,1],[3,2,7]]))
print(solution(5, [[3,7,2,0,1],[2,8,0,9,1],[1,2,1,8,1],[9,8,9,2,0],[3,6,5,1,5]]))
print(solution(7, [[9,0,5,1,1,5,3],[4,1,2,1,6,5,3],[0,7,6,1,6,8,5],[1,1,7,8,3,2,3],[9,4,0,7,6,4,1],[5,8,3,2,4,8,3],[7,4,8,4,8,3,4]]))