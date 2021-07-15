# --- 백준 스타일 ---

from sys import stdin

N = int(input())
sequence = list(map(int, stdin.readline().split()))
find_fixed_p = False
start = 0
end = N

while start <= end:
    mid = (start+end) // 2
    
    if sequence[mid] == mid:
        find_fixed_p = True
        break
    elif sequence[mid] < mid:
        start = mid + 1
    else:
        end = mid - 1

if find_fixed_p:
    print(mid)
else:
    print(-1)