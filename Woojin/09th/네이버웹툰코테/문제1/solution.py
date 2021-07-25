def solution(S, pattern):
    S_len = len(S)
    p_len = len(pattern)
    p_sorted = sorted(pattern)
    answer = 0
    
    for i in range(S_len - p_len + 1):
        if sorted(S[i:i + p_len]) == p_sorted:
            answer += 1
    
    return answer