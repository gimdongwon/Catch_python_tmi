arr = list(map(int, input().split()))
n = int(input())

# arr = {-15, -4, 2, 8, 13} 출력값 result = 2

start, end = 0, len(arr) - 1

while start <= end:
    mid = (start + end) // 2
    if mid > arr[mid]:
        start = mid + 1
    elif mid < arr[mid]:
        end = mid - 1
    else:
        print(mid)

print(start, end, mid)