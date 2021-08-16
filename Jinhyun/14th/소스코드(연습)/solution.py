# 특정 원소 속한 집합 찾기
def find_parent(parent, x) :
    if parent[x] != x :
        return find_parent(parent, parent[x])
    return x

# 두 원소 속한 집합 찾기
def union_parent(parent, a, b) :
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b :
        parent[b] = a
    else :
        parent[a] = b
    return parent

def coprime_set() :
    # 노드의 개수와 간선(union연산)의 개수 입력 받기
    v, e = map(int, input().split())
    # 부모테이블 초기화
    parent = [0] * (v + 1)
    for i in range(1, v + 1) :
        parent[i] = i

    # union 연산 각각 수행
    for i in range(e) :
        a, b = map(int, input().split())
        union_parent(parent, a, b)

    # 각 원소가 속한 집합 출력
    print('각 원소가 속한 집합 : ', end=' ')
    for i in range(1, v + 1) :
        print(find_parent(parent, i), end = ' ')

    print()

    # 부모 테이블 내용 출력
    print('부모 테이블 : ', end=' ')
    for i in range(1, v + 1) :
        print(parent[i], end = ' ')

def cycle() :
    v, e = map(int, input().split())
    parent = [0] * (v + 1)
    for i in range(1, v + 1) :
        parent[i] = i
    cycle = False # 사이클 발생 여부
    for i in range(e) :
        a, b = map(int, input().split())
        if find_parent(parent, a) == find_parent(parent, b) :
            cycle = True
            break
        else :
            union_parent(parent, a, b)
    if cycle :
        print('사이클이 발생했습니다.')
    else :
        print('사이클이 발생하지 않았습니다.')

def kruskal() :
    v, e = map(int, input().split())
    parent = [0] * (v + 1)
    for i in range(1, v + 1) :
        parent[i] = i
    edges = [] # 모든 간선 담을 리스트
    result = 0 # 최종 비용 담을 변수

    for _ in range(e) :
        a, b, cost = map(int, input().split())
        edges.append((cost, a, b))

    edges.sort() # 값 기준 정렬

    for edge in edges :
        cost, a, b = edge
        if find_parent(parent, a) != find_parent(parent, b) :
            union_parent(parent, a, b)
            result += cost

    print(result)

kruskal()