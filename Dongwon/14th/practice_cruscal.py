v,e = map(int, input().split())

# nodes = [map(int, input().split()) for _ in range(e)]

graph =  []

def find_parent(parent, x):
    if x != parent[x]:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a,b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

parent = [i for i in range(1,v+1)]
edges = []
result = 0

for _ in range(e):
    a,b,cost = map(int, input().split())
    edges.append((cost, a,b))

edges.sort()

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a,b)
        result += cost 
print(result)