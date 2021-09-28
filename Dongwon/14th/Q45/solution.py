from collections import defaultdict
# T = int(input())
n = int(input())

parent = [i for i in range(1,n+1)]

rank_last = list(map(int, input().split()))
m = int(input())
indegree = defaultdict(list)
graph = defaultdict(int)
for i in range(n-1):
    graph[rank_last[i]] = rank_last[i+1:]
    indegree[rank_last[i+1]] = i+1

for _ in range(m):
    a,b = map(int, input().split())
    if b in graph[a]:
        graph[b].append(a)
        graph[a].remove(b)

        indegree[a] += 1
        indegree[b] -= 1
    else:
        graph[a].append(b)
        graph[b].append(a)

        indegree[a] -= 1
        indegree[b] += 1

p = []

for c in rank_last:
    if indegree[c] == 0:
        p.append(c)
ans = []
while p:
    cur = p.pop()
    ans.append(cur)
    for i in graph[cur]:
        indegree[i] -= 1

        if indegree[i] == 0:
            p.append(i)
print(ans)
if len(ans) == n:
    print(*ans)
else:
    print("IMPOSIIBLE")