import collections
import heapq


# 풀이 1. 테스트 케이스 1번만 맞음.
# 정방향 그래프와 역방향 그래프를 따로 저장
# 트랩에 걸리면 그래프를 바꿔서 큐에 삽입.
def solution(n, start, end, roads, traps):
    graph = collections.defaultdict(list)
    graph_reverse = collections.defaultdict(list)

    reverse = False

    # 그래프 인접 리스트 구성 [출발 지점]:(도착지점, 소요시간)
    for u, v, w in roads:
        graph[u].append((v, w))
        graph_reverse[v].append((u, w))

    # 큐 변수: [(소요시간, 도착지점)]
    q = [(0, start)]
    dist = collections.defaultdict(int)

    while q:
        time, node = heapq.heappop(q)
        if node not in dist:
            dist[node] = time
            if node in traps:
                reverse = not reverse
            if reverse:
                for v, w in graph_reverse[node]:
                    alt = time + w
                    heapq.heappush(q, (alt, v))
            elif not reverse:
                for v, w in graph[node]:
                    alt = time + w
                    heapq.heappush(q, (alt, v))

    print(dist[end])
    return dist[end]


solution(3, 1, 3, [[1, 2, 2], [3, 2, 3]], [2])
solution(4, 1, 4, [[1, 2, 1], [3, 2, 1], [2, 4, 1]], [2, 3])
