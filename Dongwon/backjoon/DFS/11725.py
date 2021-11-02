import sys

input = sys.stdin.readline

n = int(input())

graph = [[] for _ in range(n+1)]
parents = [0 for _ in range(n+1)]

for _ in range(1,n):
    a,b = list(map(int, input().split()))
    graph[a].append(b)
    graph[b].append(a)

def dfs(x, tree, parents):
    for i in tree[x]:
        if parents[i] == 0:
            parents[i] = x
            dfs(i, tree, parents)
            
dfs(1, graph, parents)

for i in range(2, len(parents)):
    print(parents[i])