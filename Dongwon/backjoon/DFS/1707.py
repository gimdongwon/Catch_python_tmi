import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
t = int(input())

def dfs(v, group):
    visited[v] = group
    for i in graph[v]:
        if visited[i] == 0:
            if not dfs(i, -group):
                return False
        elif visited[i] == visited[v]:
            return False
    return True

for _ in range(t):
    V,E = map(int, input().split())

    graph = [[] for _ in range(V+1)]
    visited =[0] * (V+1)
    flag = True

    for _ in range(E):
        x,y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)


    for i in range(1,V+1):
        if visited[i] == 0:
            flag = dfs(i,1)
            if not flag:
                break
    print('YES' if flag else 'NO')