# -*- coding: utf-8 -*-
"""
1 ~ N 까지의 도시, M개의 단방향 도로 존재
모든 도로 거리 1
특정 도시 X로부터 출발하여 도달할 수 있는 모든 도시중 최단거리가 정확히 K인 모든 도시의 번호 출력 프로그램
출발도시 x에서 출발도시 x로 가는 최단거리 항상 0이라고 가정
"""

from collections import deque


def solution(first_line, second_line):
    n, m, k, x = map(int, first_line.split())
    second = list(map(int, second_line.split()))
    path = [[] for _ in range(n + 1)]
    for i in range(1, len(second), 2):
        path[second[i - 1]].append(second[i])

    answer = []
    dist = [-1] * (n + 1)
    dist[x] = 0
    que = deque([x])

    while que:
        now = que.popleft()
        for i in path[now]:
            if dist[i] == -1:
                dist[i] = dist[now] + 1  # 출발점 기준 거리
                que.append(i)
    for i, val in enumerate(dist):
        if val == k:
            answer.append(i)
    if len(answer) == 0:
        return -1
    return answer


# 1 -> 2 3 -> 3 4 -> 4
print(solution("4 4 2 1", "1 2 1 3 2 3 2 4"))
print(solution("4 3 2 1", "1 2 1 3 1 4"))
print(solution("4 4 1 1", "1 2 1 3 2 3 2 4"))
