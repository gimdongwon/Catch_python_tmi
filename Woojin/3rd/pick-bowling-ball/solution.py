from itertools import combinations

N, M = map(int, input().split(" "))
K = list(map(int, input().split(" ")))

comb = list(combinations(K, 2))
result = len(comb)

for c in comb:
    if c[0] == c[1]:
        result -= 1
        
print(result)