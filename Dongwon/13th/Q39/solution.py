import heapq

INF = int(1e9)

n = int(input())

dx = [-1,1,0,0]
dy = [0,0,-1,1]

graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

distance = [[INF] * n for _ in range(n)]

x,y = 0,0

q = [(graph[x][y], x, y)]
heapq.heapify(q)
distance[x][y] = graph[x][y]

# bfs 풀이법과 유사
while q:
    dist, x,y = heapq.heappop(q)
    if distance[x][y] < dist:
        continue
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if -1 < nx < n and -1 < ny < n:
            cost = dist + graph[nx][ny]
            if cost < distance[nx][ny]:
                distance[nx][ny] = cost
                heapq.heappush(q, (cost, nx, ny))

print(distance)
