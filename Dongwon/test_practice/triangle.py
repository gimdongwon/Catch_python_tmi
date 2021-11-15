def solution(A):
    A.sort()
    if len(A) < 3:
        return 0
    for i in range(len(A)-2):
        p,q,r = A[i],A[i+1],A[i+2]
        if p + q > r:
            return 1
    return 0