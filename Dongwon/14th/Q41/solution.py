n, m = map(int, input().split())



nums = []
result = True
plan = list(map(int, input().split()))


def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return x

def union_parent(parent, a,b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

parent = [0] * (n+1)
for i in range(n+1):
    parent[i] = i

for i in range(n):
    graph = list(map(int, input().split()))
    for j in range(n):
        if graph[j] == 1:
            union_parent(parent, i+1, j+1)

for i in range(m-1):
    if find_parent(parent, plan[i]) != find_parent(parent, plan[i+1]):
        result = False

print("YES" if result else "NO")