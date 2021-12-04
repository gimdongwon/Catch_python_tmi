t = int(input())

for _ in range(t):
    n,m = map(int, input().split())
    arr = list(map(int, input().split()))
    temp = arr[:]
    for idx, item in enumerate(arr):
        arr[idx] = (item, idx)
    target = arr[m]
    result = 0
    while arr:
        if max(temp) == arr[0][0]:
            result += 1
            temp.remove(max(temp))
            if not arr or arr.pop(0) == target:
                break
        else:
            arr.append(arr.pop(0))
        
    print(result)