n = int(input())

arr = [int(input()) for _ in range(n)]

arr.sort(reverse=True)
result = []
for item in range(n):
    result.append(arr[item] * (item+1))

print(max(result))