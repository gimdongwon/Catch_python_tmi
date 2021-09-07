import collections
import heapq


# 풀이 2. 역시 정확성 실패
# 그래프 만들때 방향 정보 포함
def solution2(n, start, end, roads, traps):
    graph = collections.defaultdict(list)

    reverse = False

    # 그래프 구성 [출발 지점]:(도착지점, 소요시간, 방향)
    for u, v, w in roads:
        graph[u].append((v, w, True))  # 정방향
        graph[v].append((u, w, False))  # 역방향

    # 큐 변수: [(소요시간, 도착지점, 방향)]
    q = [(0, start, True)]
    dist = collections.defaultdict(int)

    while q:
        time, node, direction = heapq.heappop(q)
        if node not in dist:
            if reverse:
                if not direction:
                    dist[node] = time
            elif not reverse:
                if direction:
                    dist[node] = time
            if node in traps:
                reverse = not reverse
            for v, w, trap in graph[node]:
                alt = time + w
                heapq.heappush(q, (alt, v, trap))

    print(dist[end])
    return dist[end]


# solution2(3, 1, 3, [[1, 2, 2], [3, 2, 3]], [2])
solution2(4, 1, 4, [[1, 2, 1], [3, 2, 1], [2, 4, 1]], [2, 3])
