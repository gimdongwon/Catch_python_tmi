import sys
input = sys.stdin.readline

n = int(input())
result = []
for _ in range(n):
    x,y = map(int, input().split())
    result.append((x,y))

result.sort(key=lambda x: [x[0],x[1]])

for x,y in result:
    print(x,y)