n = int(input())
result = 0
peoples = list(map(int, input().split()))
peoples.sort()

for i in range(1, n+1):
    result += peoples[-i] * i

print(result)