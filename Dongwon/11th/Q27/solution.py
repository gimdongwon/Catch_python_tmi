# N,X = map(int, input().split())
n,x = 7,2
nums = [1,1,2,2,2,2,3]

left,right = 0, len(nums)-1

def find_left(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            if mid - 1 < 0 or arr[mid-1] != target:
                return mid
            else:
                end = mid - 1
        elif arr[mid] >= target:
            end = mid - 1
        else:
            start = mid + 1
    return -1

def find_right(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            if mid + 1 >= len(arr) or arr[mid+1] != target:
                return mid
            else:
                start = mid + 1
        elif arr[mid] >= target:
            end = mid - 1
        else:
            start = mid + 1
    return -1

l = find_left(nums, x, left, right)
r = find_right(nums, x, left, right)

print(l,r)

if l == -1 or r == -1:
    # 하나도 없는 경우
    print(-1)
else:
    # l이상 r개 이하이므로 + 1
    print(r - l + 1)

# bisect 사용

def bisect_solution():
    from bisect import bisect_left, bisect_right
    N,x = map(int, input().split())
    arr = list(map(int, input().split()))

    # arr에서 x를 삽입할 가장 왼쪽, 오른쪽 값을 찾음.
    count = bisect_left(arr, x) - bisect_right(arr,x)
    print(bisect_left(arr, x), bisect_right(arr,x))
    if count == 0:
        print(-1)
    else:
        print(count)

bisect_solution()