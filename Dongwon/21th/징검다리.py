# 1차 시도 완탐

from itertools import combinations

def solution(distance, rocks, n):
    answer = []
    temp = list(combinations(rocks, len(rocks)- n))
    for item in temp:
        target = list(item)
        target.extend([0,distance])
        target.sort()
        result = []
        for i in range(len(target)-1):
            result.append(target[i+1] - target[i])
    
        answer.append(min(result))
        
    return max(answer)

# 2차 이분탐색

def solution(distance, rocks, n):
    rocks.append(distance)
    rocks.sort()
    left, right = 0, distance
    result = 0
    
    while left <= right:
        mid = (left + right) // 2
        remove_stone = 0
        min_num = 1000000000
        current = 0 # 0부터 시작
        # 돌의 갯수
        for rock in rocks:
            if rock - current < mid:
                remove_stone += 1
            else:
                min_num = min(min_num, rock - current)
                current = rock
        # 제거된 돌의 갯수로 left, right 값 재 설정
        if remove_stone <= n:
            left = mid + 1
            result = min_num
        else:
            right = mid - 1
    return result

# 3차 함수 분리

def solution(distance, rocks, n):
    rocks.append(distance)
    rocks.sort()
    left, right = 0, distance
    result = 0
    
    while left <= right:
        mid = (left + right) // 2
        remove_stone = 0
        min_num = 1000000000
        remove_stone, min_num = remove_stones_fn(rocks, mid, remove_stone, min_num)
        # 제거된 돌의 갯수로 left, right 값 재 설정
        if remove_stone <= n:
            left = mid + 1
            result = min_num
        else:
            right = mid - 1
    return result

def remove_stones_fn(rocks, mid, remove_stone, min_num):
    current = 0 # 0부터 시작
    # 돌의 갯수
    for rock in rocks:
        if rock - current < mid:
            remove_stone += 1
        else:
            min_num = min(min_num, rock - current)
            current = rock
    return remove_stone, min_num