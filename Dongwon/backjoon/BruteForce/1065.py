n = int(input())

result = 0

for i in range(1, n+1):
    if i <= 99:
        result += 1
    else:
        arr = list(map(int, str(i)))
        if arr[1] - arr[0] == arr[2] - arr[1]:
            result+=1

print(result)