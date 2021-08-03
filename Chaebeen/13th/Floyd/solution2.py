# coding=utf-8
import collections
import heapq


#다익스트라 풀이
def solution2(n, price):
    graph = collections.defaultdict(list)

    for u, v, w in price:
        graph[u].append((v, w))

    result = []

    # dist: [도착지점: 최소비용]
    for i in range(1, n + 1):
        q = [(0, i)] # q: [(비용, 도착지점)]
        dist = collections.defaultdict(int)
        while q:
            distance, node = heapq.heappop(q)
            if node not in dist:
                dist[node] = distance
                for v, w in graph[node]:
                    alt = distance + w
                    heapq.heappush(q, (alt, v))
        print(dist)
        result.append(list(dist.values()))

    for i in range(n):
        print(result[i])


solution2(5, [[1, 2, 2], [1, 3, 3], [1, 4, 1], [1, 5, 10], [2, 4, 2],
                 [3, 4, 1], [3, 5, 1], [4, 5, 3], [3, 5, 10], [3, 1, 8],
                 [1, 4, 2], [5, 1, 7], [3, 4, 2], [5, 2, 4]])