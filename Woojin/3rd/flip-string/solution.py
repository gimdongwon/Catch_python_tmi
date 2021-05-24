def solution(s):
    result = 1
    
    # 0 그룹의 개수와 1 그룹의 개수를 더하면 result
    for i, char in enumerate(s[:-1]):
        if char != s[i + 1]:
            result += 1
            
    return result // 2 # 0 그룹의 개수와 1 그룹의 개수 중 작은 값 반환

print(solution("1010"))