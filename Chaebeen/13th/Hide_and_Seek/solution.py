# coding=utf-8
import collections
import heapq


def solution(n, m, rooms):
    graph = collections.defaultdict(list)

    # 그래프 인접 리스트 구성 [출발 지점:[도착지점]]
    # 양방향 [도착지점:[출발지점]]
    for u, v in rooms:
        graph[u].append(v)
        graph[v].append(u)

    # 큐 변수: [(이동거리, 도착지점)]
    # 1번에서 출발 초기화 (1번까지 이동거리 0)
    q = [(0, 1)]
    dist = collections.defaultdict(int)

    # dist: [도착지점: 이동거리]
    while q:
        distance, node = heapq.heappop(q)
        if node not in dist:
            dist[node] = distance
            for v in graph[node]:
                alt = distance + 1
                heapq.heappush(q, (alt, v))

    dist_list = list(dist.values())  # 리스트로 변환
    max_distance = max(dist_list)  # 가장 먼 거리
    hide_room = dist_list.index(max_distance) + 1  # 가장 먼 거리의 방 번호
    other_rooms = dist_list.count(max_distance)  # 같은 거리의 방 개수

    return hide_room, max_distance, other_rooms


print(solution(6, 7, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))
print(solution(6, 7, [[3, 6], [4, 3], [3, 5], [1, 3], [1, 5], [5, 4], [2, 5]]))

