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

def solution(n, x, y, z) :
    parent = [i for i in range(n)]
    x_coord = list(map(int, x.split()))
    y_coord = list(map(int, y.split()))
    z_coord = list(map(int, z.split()))

    edges = []

    for i in range(n) :
        for j in range(i, n) :
            cost = min(abs(x_coord[i]-x_coord[j]), abs(y_coord[i]-y_coord[j]), abs(z_coord[i]-z_coord[j]))
            edges.append((cost, i, j))
    
    edges.sort()

    result = 0
    for edge in edges :
        cost, start, end = edge
        if find_parent(parent, start) != find_parent(parent, end) :
            union_parent(parent, start, end)
            result += cost
    
    return result

print(solution(5, '11 14 -1 10 19', '-15 -5 -1 -4 -4', '-15 -15 -5 -1 19'))
    