n,k = map(int, input().split())

result = 0
arr = [True] * (n+1)

for i in range(2, len(arr)+1):
    for j in range(i, n+1, i):
        if arr[j] == True:
            arr[j] = False
            result += 1
            if result == k:
                print(j)
                break