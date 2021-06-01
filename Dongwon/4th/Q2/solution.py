def solution(S):
    # p = list(map(int, list(S))) # 여기를 좀 고치고 싶은데..
    p = list(map(int, S))
    # p.sort()
    # result = 1 if p[0] == 0 else p[0]
    result = 0
    for item in p:

        if item == 0 or item == 1:
            result += item
        else:
            if result == 0:
                result += item
            else:
                result *= item
                
    print(result)
    return result


solution("02984")
solution("567")