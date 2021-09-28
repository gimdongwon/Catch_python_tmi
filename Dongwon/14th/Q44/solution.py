# 행성 터널 크루스칼 알고리즘.
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n = int(input())
planets = []

for _ in range(n):
    x,y,z = map(int, input().split())
    planets.append((x,y,z))

