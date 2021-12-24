def solution(a):
    answer = 1
    start = a[0]
    for i in range(1, len(a)):
        if start > a[i]:
            answer += 1
            start = a[i]
    start = a[-1]
    
    for i in range(len(a)-2,-1, -1):
        if start > a[i]:
            answer += 1
            start = a[i]
    return answer