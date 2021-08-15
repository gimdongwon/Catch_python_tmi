# 총 비용 - 최소 비용 = 최대 절약 비용
# 모든 노드를 연결하는 최소 비용?
# 크루스칼 알고리즘


def get_parent(parent, x):
    if parent[x] == x:
        return parent[x]
    return get_parent(parent, parent[x])


# 숫자가 작은 부모로 병합
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
    if a == b:
        return False
    else:
        return True


def solution(n, m, street):
    dp = []
    result = 0

    parent = [i for i in range(n)]  # 부모를 각 노드로 초기화

    for i in street:
        x, y, cost = i
        dp.append((cost, x, y))

    dp.sort()  # 비용 순으로 정렬

    total_cost = 0
    min_cost = 0
    for cost, x, y in dp:
        total_cost += cost
        # 부모가 다른 경우(사이클이 발생하지 않는 경우)
        if different_parent(parent, x, y):
            min_cost += cost
            union_parent(parent, x, y)

    print(total_cost - min_cost)  # 총 비용 - 최소 비용 = 최대 절약 비용


solution(7, 11,
         [[0, 1, 7],
          [0, 3, 5],
          [1, 2, 8],
          [1, 3, 9],
          [1, 4, 7],
          [2, 4, 5],
          [3, 4, 15],
          [3, 5, 6],
          [4, 5, 8],
          [4, 6, 9],
          [5, 6, 11]])
