import sys
input = sys.stdin.readline
from  collections import defaultdict, deque

n,m = map(int, input().split())

trust_relation = [[] for _ in range(n+1)]
max_cnt = 0
answer = []
for _ in range(m):
    a,b = map(int, input().split())
    trust_relation[b].append(a)

def dfs(start):
    cnt = 0
    visited = [False for _ in range(n+1)]
    visited[start] = True
    stack = []
    stack.append(start)
    while stack:
        target = stack.pop()
        for j in trust_relation[target]:
            if visited[j] == False:
                stack.append(j)
                visited[j] = True
                cnt += 1
    return cnt
    
for i in range(1, n+1):
    cnt = dfs(i)
    if cnt > max_cnt:
        max_cnt = cnt
    answer.append([i, cnt])

for i, cnt in answer:
    if cnt == max_cnt:
        print(i, end=' ')