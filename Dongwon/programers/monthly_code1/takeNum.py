from itertools import combinations

def solution(numbers):
    arr = list(combinations(numbers, 2))
    answer = []
    for item in arr:
        if sum(item) not in answer:
            answer.append(sum(item))
    answer.sort()
    return answer