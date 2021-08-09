# x, y, z 거리 비용을 따로 구해서 하나의 그래프로 만들기
# x, y, z 기준으로 각각 정렬 후 옆 노드와 차를 구하면 가장 가까운 거리를 알 수 있음.
# 크루스칼 알고리즘
def get_parent(parent, x):
    if parent[x] == x:
        return parent[x]
    return get_parent(parent, parent[x])


def union_parent(parent, x, y):
    a = get_parent(parent, x)
    b = get_parent(parent, y)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def different_parent(parent, x, y):
    a = get_parent(parent, x)
    b = get_parent(parent, y)

    if a != b:
        return True
    else:
        return False


def solution(n, planet):
    dp = []
    parent = [i for i in range(n)]
    result = 0

    # x, y, z 기준으로 정렬
    planet_x = sorted(planet, key=lambda x: x[0])
    planet_y = sorted(planet, key=lambda x: x[1])
    planet_z = sorted(planet, key=lambda x: x[2])

    for i in range(n - 1):
        dp.append((planet_x[i + 1][0] - planet_x[i][0], i, i + 1))
        dp.append((planet_y[i + 1][1] - planet_y[i][1], i, i + 1))
        dp.append((planet_z[i + 1][2] - planet_z[i][2], i, i + 1))

    dp.sort()

    for cost, a, b in dp:
        if different_parent(parent, a, b):
            result += cost
            union_parent(parent, a, b)

    print(result)


solution(5,
         [[11, -15, -15],
          [14, -5, -15],
          [-1, -1, -5],
          [10, -4, -1],
          [19, -4, 19]])
