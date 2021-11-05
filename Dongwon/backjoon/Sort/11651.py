n = int(input())

childrens = []

for _ in range(n):
    x, y = map(int, input().split())
    childrens.append((x,y))

childrens.sort(key=lambda x: (x[1], x[0]))

for x,y in childrens:
    print(x,y)