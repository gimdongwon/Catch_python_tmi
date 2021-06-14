# coding=utf-8
from itertools import combinations
from itertools import product


def solution(n, m, city):
    city_map = [[0] * n for _ in range(n)]
    home_list = []
    chicken_list = []
    result = []

    for i in range(n):
        for j in range(n):
            city_map[i][j] = city[(i * n) + j]

    for i in range(n):
        for j in range(n):
            if city_map[i][j] == 1:
                home_list.append([i, j])
            elif city_map[i][j] == 2:
                chicken_list.append([i, j])

    open_chicken = list(combinations(chicken_list, m))

    for i in range(len(open_chicken)):  # 선택될 수 있는 치킨집 경우의 수
        city_distance = 0
        for x, y in home_list:
            distance = []  # 모든 경우 치킨 거리
            for p, q in open_chicken[i]:
                distance.append(abs(x - p) + abs(y - q))
            city_distance += min(distance)  # 제일 가까운 거리만 도시 치킨 거리에 더함
        result.append(city_distance)  # 구해진 도시 치킨 거리들을 결과값에 저장

    print(min(result))  # 최소값 출력


solution(3, 3, [2, 0, 1, 2, 0, 2, 2, 1, 2])
