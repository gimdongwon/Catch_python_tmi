# 토마토 7569

[링크](https://www.acmicpc.net/problem/7569)

골드5답게 굉장히 어려운 문제였다. 나는 아직 골드가 어렵다. 하지만 레벨은 골드임..

하지만 좀 만 더 간단하게 생각해보면 그리 어렵지 않다. 기존에 자주 하던 bfs 탐색에서 floor라는 개념이 추가된 것으로 df를 추가해 주었다.

exit(0)을 하면 프로그램이 종료된다. break를 해도 작동하니 알아두는 정도로 하고 넘어가자.

```py3
from collections import deque
import sys
input = sys.stdin.readline

m,n,h = map(int, input().split())
dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
df = [0,0,0,0,-1,1]
day = 0
tomatos = []
queue = deque([])

for f in range(h):
    temp = []
    for i in range(n):
        temp.append(list(map(int, input().split())))
        for j in range(m):
            if temp[i][j] == 1:
                queue.append([day,[f,i,j]])
    tomatos.append(temp)

while queue:
    day, which = queue.popleft()
    f,x,y = which
    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nf = f + df[i]
        if -1 < nf < h and -1 < nx < n and -1 < ny < m and tomatos[nf][nx][ny] == 0:
            queue.append([day+1, [nf,nx,ny]])
            tomatos[nf][nx][ny] = tomatos[f][x][y] + 1

for tomato in tomatos:
    for item in tomato:
        for j in item:
            if j == 0:
                print(-1)
                exit(0)
        day = max(day, max(item))
print(day-1)
```
