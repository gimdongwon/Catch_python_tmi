from itertools import combinations

def solution(A):
    result = -10 ** 9
    A.sort()
    if len(A) >= 6:
        for a,b,c in combinations(A[:3] + A[-3:],3):
            result = max(result, a*b*c)
    else:
        for a,b,c in combinations(A,3):
            result = max(result, a*b*c)
    return result