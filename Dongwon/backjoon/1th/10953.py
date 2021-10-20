n = int(input())

for _ in range(n):
    s = list(map(int, input().split(",")))
    print(sum(s))