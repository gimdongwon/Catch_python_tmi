'''
    고정점이란 : 수열의 원소 중에서 그 값이 인덱스와 동일한 원소
    하나의 수열이 N개의 "서로다른 원소" 포함하고 있으며, 모든 원소가 오름차순으로 정렬되어 있습니다.
    고정점은 최대 한개 존재합니다
'''

def search_fixed_point(start, end, array) :
    if start > end :
        return -1
    mid = (start + end) // 2
    if array[mid] == mid :
        return mid
    else :
        if array[mid] > mid :
            return search_fixed_point(start, mid - 1, array)
        else :
            return search_fixed_point(mid + 1, end, array)

def solution(n, seq) :
    seq = list(map(int, seq.split()))
    start = 0
    end = n
    return search_fixed_point(start, end, seq)

print(solution(5,'-15 -6 1 3 7'))
print(solution(7, '-15 -4 2 8 9 13 15'))
print(solution(7, '-15 -4 3 8 9 13 15'))

