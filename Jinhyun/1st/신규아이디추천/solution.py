def solution(new_id):
    special_char = "~!@#$%^&*()=+[{]}:?,<>/"
    # 1단계, 2단계
    answer = ''.join([i.lower() for i in new_id if i not in special_char])
    # 3단계
    answer = answer.strip('.')
    # 4단계 => filter를 통해서 split시 빈 문자열 제외
    answer = '.'.join(filter(None, answer.split('.')))
    # 5단계
    if len(answer) == 0 :
        answer = 'a'
    # 6단계 (혹시 들어갈 마침표 대비 strip)
    if len(answer) >= 16 :
        return answer[:15].strip('.')
    # 7단계 1개 아니면 2개이지만 혹시나 모든 경우 대비 list
    elif len(answer) <= 2 :
        answer += ''.join([answer[-1] for _ in range(3 - len(answer))])
        return answer
    else :
        return answer
