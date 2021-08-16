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

def solution(g, p, g_i) :
    parent = [i for i in range(g + 1)]
    result = 0
    g_i = list(map(int, g_i.split()))
    for i in range(p) :
        root = find_parent(parent, g_i[i])
        if root == 0 :
            break
        else :
            union_parent(parent, root-1, root)
            result += 1    
    return result

print(solution(4, 3, '4 1 1'))
'''
4 : 1번부터 4번까지 도킹 가능 -> 4번에 도킹
    -> 만약 4번이 또 들어왔다면 -> 4번에서 3번으로 보내야함 -> 그래서 union_parent를 root-1과 root
1 : 1번부터 1번까지 도킹 가능 -> 1번에 도킹
1 : 1번부터 1번까지 도킹 가능 -> 1번에 도킹 -> 이미 있음 -> 부모를 찾을 때 : 0으로 간다 끝~
'''
print(solution(4, 6, '2 2 3 3 4 4'))
'''
2 : 1번부터 2번까지 도킹 가능 -> 2번에 도킹 (부모는 1번)
2 : 1번부터 2번까지 도킹 가능 -> 2번에 도킹 못함 -> 1번에 도킹 (부모는 0번)
3 : 1번부터 3번까지 도킹 가능 -> 3번에 도킹 (부모는 2번 -> 부모는 0번)
3 : 1번부터 3번까지 도킹 가능 -> 3번에 도킹 못함 -> 0번으로 이동 == break
'''