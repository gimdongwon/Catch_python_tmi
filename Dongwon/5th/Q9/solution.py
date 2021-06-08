def solution(s):
    # test 5 반례 엣지 케이스
    if len(s)==1:
        return 1
    
    result = []
    # 자를 수 있는 최대 수는 s의 최대길이의 절반
    for x in range(1, len(s)//2+1):
        # str_group는 잘라지는 str 모음
        str_group = []
        for i in range(0, len(s), x):
            str_group.append(s[i:i+x])
        num = 1
        # 최소 길이가 될 수 있는 후보들
        candidates = []
        for i in range(len(str_group)-1):
            # 같으면 num만 증가
            if str_group[i] == str_group[i+1]:
                num += 1
            # 다르면 숫자와 str 합쳐서 candidates에 넣어주기
            else:   
                if num > 1:
                    candidates.append(str(num)+str_group[i])
                    num = 1
                else:
                    candidates.append(str_group[i])
            # 마지막일 때만 따로 처리
            if i == len(str_group) - 2:
                if num > 1:
                    candidates.append(str(num)+str_group[i+1])
                else:
                    candidates.append(str_group[i+1])
        result.append("".join(candidates))
    return min(list(map(lambda x: len(x), result)))