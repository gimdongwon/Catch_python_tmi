from collections import Counter
import sys
input = sys.stdin.readline

n = int(input())

arr = [int(input()) for _ in range(n)]
arr.sort()

print(round(sum(arr)/len(arr)))
print(arr[len(arr)//2])
if len(arr) > 1:
    target = Counter(arr).most_common()
    target.sort(key=lambda x: [-x[1], x[0]])
    print(target[0][0] if target[0][1] > target[1][1] else target[1][0])
else:
    print(arr[0])

print(arr[-1]-arr[0])