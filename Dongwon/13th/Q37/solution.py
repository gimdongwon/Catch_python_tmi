INF = int(1e9)

n,m = map(int, input().split())

graph = [[INF] * (n+1) for _ in range(n+1)]

# 자기 자신에게 가는 경우 0으로 초기화
for a in range(1, n+1):
    for b in range(1,n+1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    a,b,c = map(int, input().split())
    if c < graph[a][b]:
        graph[a][b] = c
print(graph)
# 플로이드 워셜 점화식 ! 기억하기
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF:
            print(0, end=' ')
        else:
            print(graph[a][b], end=' ')
    print() # 줄바꿈
# print(graph)