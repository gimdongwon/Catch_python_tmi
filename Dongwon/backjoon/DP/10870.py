n = int(input())

arr = [0,1]

i = 1

while i < n:
    i+=1
    arr.append(arr[len(arr)-1]+arr[len(arr)-2])

print(arr[-1] if n != 0 else 0)