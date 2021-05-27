def solution(S):
    p = list(map(int, list(S))) # 여기를 좀 고치고 싶은데..
    p.sort()
    result = 1 if p[0] == 0 else p[0]
    
    for i in range(1, len(p)):
        result *= p[i]
        
    print(result)
    return result


solution("02984")
solution("567")