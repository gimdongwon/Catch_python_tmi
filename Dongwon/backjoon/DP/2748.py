n = int(input())

arr = [0,1]

i = 2

while i <= n:
    arr.append(arr[i-2] + arr[i-1])
    i += 1

print(arr[-1])