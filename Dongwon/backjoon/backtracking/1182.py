from itertools import combinations

n,s = map(int, input().split())

arr = list(map(int, input().split()))
result = 0

for i in range(1, n+1):
    for jtem in list(combinations(arr, i)):
        if sum(jtem) == s:
            result += 1
    
print(result)