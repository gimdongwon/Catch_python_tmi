n = int(input())

peoples = [tuple(map(int, input().split())) for _ in range(n)]
result = []

for x,y in peoples:
    result.append(len(list(filter(lambda a: a[0] > x and a[1] > y, peoples)))+1)

print(" ".join(list(map(str, result))))