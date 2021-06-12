from itertools import groupby

# 압축 단위가 n일 때, 압축된 문자열의 길이(compressed string length)를 반환하는 함수
def get_comp_str_len(s, n):
    splited_str_list = []    # 문자열 s를 n개 단위로 자른 문자열들을 저장한 배열
    compressed_str_list = [] # 압축된 문자열을 저장한 배열
    
    for i in range(0, len(s), n):
        splited_str_list.append(s[i:i + n])

    """
    groupby()를 이용해 연속된 문자열의 개수를 구할 수 있음
    """
    for x, group in groupby(splited_str_list):
        group_len = len(list(group))
        
        if group_len == 1:
            compressed_str_list.append(x)
        else:
            compressed_str_list.append(f"{group_len}{x}")
    
    return sum(len(c) for c in compressed_str_list)

def solution(s):
    # 예외 처리 (s의 길이가 1일 때)
    if len(s) == 1:
        return 1
    
    # 압축 단위는 1부터 (len(s) // 2)까지
    result_list = []
    
    for i in range(1, (len(s)//2) + 1):
        result_list.append(get_comp_str_len(s, i))
        
    return min(result_list)