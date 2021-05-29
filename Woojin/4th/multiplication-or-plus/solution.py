# 풀이 1 (직관적인 풀이)
def solution(s):
    s_list = list(map(int, s))
    
    while len(s_list) >= 2:
        if s_list[0] + s_list[1] >= s_list[0] * s_list[1]:
            s_list[:2] = [s_list[0] + s_list[1]]
        else:
            s_list[:2] = [s_list[0] * s_list[1]]
    
    return s_list[0]

# 풀이 2 (좀 더 효율적인 풀이)
def solution(s):
    s_list = list(map(int, s))
    
    while len(s_list) >= 2:
        if 0 in s_list[:2] or 1 in s_list[:2]:
            s_list[:2] = [s_list[0] + s_list[1]]
        else:
            s_list[:2] = [s_list[0] * s_list[1]]
    
    return s_list[0]

print(solution("02984"))
print(solution("567"))
print(solution("931223"))