from itertools import combinations

a,b = map(int, input().split())
count = 0
balls = list(map(int, input().split()))

result = list(combinations(balls, 2))
print(result)
for i in range(1, b+1):
    if balls.count(i) > 1:
        count += result.count((i,i))

print(len(result) - count)
