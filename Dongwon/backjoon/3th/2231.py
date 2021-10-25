n = int(input())

for i in range(1, n+1):
    result = sum(map(int, list(str(i))))
    if result + i == n:
        print(i)
        break
else:
    print(0)