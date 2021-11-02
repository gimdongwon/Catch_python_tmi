from itertools import combinations

n,m = map(int, input().split())
cards = list(map(int, input().split()))

result = list(map(sum, list(combinations(cards, 3))))
result.sort()
print(list(filter(lambda x: x<=m, result))[-1])