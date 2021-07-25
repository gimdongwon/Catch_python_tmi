from itertools import combinations

def solution(k):
    comb = list(combinations(k, 2))
    result = len(comb)

    for c in comb:
        if c[0] == c[1]:
            result -= 1
    
    return result