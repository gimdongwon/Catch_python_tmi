n = int(input())

result = [input() for _ in range(n)]

result = list(set(result))

result.sort()
result.sort(key=len)

for item in result:
    print(item)