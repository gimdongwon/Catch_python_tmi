import collections

# 생각의 과정
# (2->3), (3->4), (4->3) 경로를 쪼개서 이동 가능한 경로인지 하나씩 체크
# (2->3), (2->4), (2->3) 출발 지점에서 각 도시로 이동 가능한지 하나씩 체크
# (2->3, 4) 출발 지점에서 계획한 모든 도시로 이동 가능한지 체크
# 결론: 계획한 도시가 출발 지점에서 갈 수 있는 모든 노드에 포함되는지?


def solution(n, m, city, plan):
    graph = collections.defaultdict(list)
    # 그래프 만들기
    for i in range(1, n + 1):
        graph[i] = [x + 1 for x in range(n) if city[i - 1][x] == 1]

    stack = [plan[0]]  # 시작 노드  = 출발 도시
    visit = []

    # DFS
    # 방문할 수 있는 모든 노드
    while stack:
        node = stack.pop()
        if node not in visit:
            visit.append(node)
            stack.extend(graph[node])

    if list(set(plan) - set(visit)):  # 방문할 도시 - 방문할 수 있는 도시
        print("NO")
    else:
        print("YES")


solution(5, 4, [[0, 1, 0, 1, 1], [1, 0, 1, 1, 0], [0, 1, 0, 0, 0], [1, 1, 0, 0, 0], [1, 0, 0, 0, 0]], [2, 3, 4, 3])
solution(5, 4, [[0, 1, 0, 1, 0], [1, 0, 1, 1, 0], [0, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 0, 0, 0]], [2, 5, 4, 3])