from itertools import combinations

n,m = map(int,input().split())

cards = list(map(int, input().split()))

result = []

for item in list(combinations(cards, 3)):
    print(item)
    if sum(item) <= m:
        result.append(sum(item))
        if sum(item) == m:
            break

result.sort()
print(result[-1])