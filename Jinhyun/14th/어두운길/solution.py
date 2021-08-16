def find_parent(parent, x) :
    if parent[x] != x :
        return find_parent(parent, parent[x])
    return x

def union_parent(parent, a, b) :
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b :
        parent[b] = a
    else :
        parent[a] = b
    return parent

# kruskal 알고리즘을 통해서 도로간 최저 cost를 구한 후 전체에서 뺴주는 형식으로 진행

def solution(n, m, start, end, cost) :
    parent = [i for i in range(n)]
    start_list = list(map(int, start.split()))
    end_list = list(map(int, end.split()))
    cost_list = list(map(int, cost.split()))

    edges = []
    for i in range(m) :
        edges.append((cost_list[i], start_list[i], end_list[i]))
    
    edges.sort()

    result = 0
    for edge in edges :
        cost, start, end = edge
        if find_parent(parent, start) != find_parent(parent, end) :
            union_parent(parent, start, end)
            result += cost
        
    return sum(cost_list) - result

print(solution(7, 11, '0 0 1 1 1 2 3 3 4 4 5', '1 3 2 3 4 4 4 5 5 6 6', '7 5 8 9 7 5 15 6 8 9 11'))