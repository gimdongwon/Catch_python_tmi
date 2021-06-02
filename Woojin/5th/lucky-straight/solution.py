def solution(N):
    N_list = list(map(int, str(N)))
    half_len = len(N_list) // 2
    
    if sum(N_list[:half_len]) == sum(N_list[half_len:]):
        return "LUCKY"
    else:
        return "READY"
    
print(solution(123402))
print(solution(931223))