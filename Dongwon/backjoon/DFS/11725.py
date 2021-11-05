import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())

graph = [[] for _ in range(n+1)]
parents = [0 for _ in range(n+1)]

for _ in range(n-1):
    a,b = list(map(int, input().split()))
    graph[a].append(b)
    graph[b].append(a)

def dfs(x, tree, parents):
    for i in tree[x]:
        if parents[i] == 0:
            parents[i] = x
            dfs(i, tree, parents)
            
dfs(1, graph, parents)

for i in range(2, n+1):
    print(parents[i])