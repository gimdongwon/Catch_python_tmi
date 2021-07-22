# --- 백준 스타일 ---

from bisect import bisect_left, bisect_right

N, x = map(int, input().split())
sequence = list(map(int, input().split()))
result = bisect_right(sequence, x) - bisect_left(sequence, x)

if result:
    print(result)
else:
    print(-1)