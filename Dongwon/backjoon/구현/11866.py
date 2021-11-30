n,k = map(int, input().split())

arr = [i for i in range(1, n+1)]
print("<", end='')
while arr:
    for i in range(k-1):
        arr.append(arr[0])
        arr.pop(0)
    print(arr.pop(0), end='')
    if arr:
        print(', ', end='')

print(">")