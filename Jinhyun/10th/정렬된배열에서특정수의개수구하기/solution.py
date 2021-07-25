# 이진탐색 함수 bisect사용
# 해당 지점에 원소를 넣기 위해서 특정 원소 왼쪽, 오른쪽에 넣을지를 결정하는 함수
from bisect import bisect_left, bisect_right

def solution(n, x, seq) :
    seq = list(map(int, seq.split()))
    # 정렬되어있는 수열에서 x가 위치한 가장 왼쪽 index
    bisect_left_val = bisect_left(seq, x)
    # 정렬되어있는 수열에서 x가 위치한 가장 오른쪽 index
    bisect_right_val = bisect_right(seq, x)
    count = bisect_right_val - bisect_left_val
    if count == 0 :
        return -1
    else :
        return count

print(solution(7,2,'1 1 2 2 2 2 3'))
print(solution(7,4,'1 1 2 2 2 2 3'))