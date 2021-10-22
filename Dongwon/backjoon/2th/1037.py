n = int(input())

arr = list(map(int, input().split()))
arr.sort()
def find_common(k):
    result = []
    for i in range(2,k):
        if k % i == 0:
            result.append(i)
    return result

target = arr[0] * arr[-1]

while True:
    candidate = find_common(target)
    if arr == candidate:
        print(target)
        break
    else:
        target += 1