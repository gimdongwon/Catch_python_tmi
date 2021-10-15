# 1차 시도

INF = 1e9

def solution(n, costs):
    graph = [[] for _ in range(n)]
    result = [INF for _ in range(n)]
    visited = [[False] * n for _ in range(n)]
    for cost in costs:
        graph[cost[0]].append([cost[1], cost[2]])
        graph[cost[1]].append([cost[0], cost[2]])
    print(graph)
    print(visited)
    for i in range(len(graph)):
        for jtem in graph[i]:
            if result[i] >= jtem[1] and visited[i] == False:
                result[i] = jtem[1]
                visited[jtem[0]] = True
        print(visited)
    print(result)
    return sum(list(filter(lambda x: x != INF, result)))