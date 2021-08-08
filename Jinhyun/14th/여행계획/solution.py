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

def solution(n, m, travel, route) :
    travel = list(map(int, travel.split()))
    travel = [travel[ro:ro+n] for ro in range(0, len(travel), n)]
    parent = [i for i in range(n + 1)]
    for i in range(n) :
        for j in range(i, n) :
            if travel[i][j] == 1 :
                parent = union_parent(parent, i+1, j+1)
    
    plan = []
    
    for ro in route :
        plan.append(find_parent(parent, ro))


    if len(set(plan)) == 1 :
        print("YES")
    else :
        print("NO")

        
solution(5, 4, '0 1 0 1 1 1 0 1 1 0 0 1 0 0 0 1 1 0 0 0 1 0 0 0 0', [2,3,4,3])