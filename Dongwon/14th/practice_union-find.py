def my_solve():
    # 서로소 집합 알고리즘 소스코드

    v,e = map(int, input().split())

    nodes = [(map(int, input().split())) for _ in range(e)] # node들

    graph = [i+1 for i in range(v+1)]

    # 부모 노드 찾기
    for a,b in nodes:
        if graph[a-1] != a:
            graph[a-1] = graph[b-1]
        else:
            if a < b:
                if graph[b-1] > a:
                    graph[b-1] = a
                else:
                    graph[a-1] = graph[b-1]
            else:
                graph[a-1] = b

    # 자기가 속한 노드집합 찾기
    result = []
    for i in range(len(graph)):
        if i+1 == graph[i]:
            result.append(i+1)
        else:
            result.append(result[i-1])


    print(graph[:-1])
    print(result[:-1])

def book_solve():
    def __init__(self) -> None:
        pass
    # 개선된 서로소 집합 알고리즘
    def find_parent(parent, x):
        if parent[x]!=x:
            parent[x] = find_parent(parent, parent[x])
        return parent[x]

    def union_parent(parent, a, b):
        a = find_parent(parent, a)
        b = find_parent(parent, b)
        if a < b:
            parent[b] = a
        else:
            parent[a] = b
    v,e = map(int, input().split())
    parent = [0] * (v+1)

    for i in range(1, v+1):
        parent[i] = 1
    
    for i in range(e):
        a,b = map(int, input().split())
        union_parent(parent, a,b)

    for i in range(1, v+1):
        print(find_parent(parent,i), end=' ')
    print()

    for i in range(1, v+1):
        print(parent[i], end=' ')
