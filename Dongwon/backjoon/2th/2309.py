from itertools import combinations

shorts = [int(input()) for _ in range(9)]
shorts = list(combinations(shorts, 7))
result = []
for short in shorts:
    if sum(short) == 100:
        result = list(short)
        break
result.sort()
for item in result:
    print(item)