def solution(s):
    # 양쪽 괄호 제거 후 가운데 문자를 통해 스플릿, 이후 ,로 재 스플릿
    s = s.lstrip('{').rstrip('}')
    s = [i.split(',') for i in s.split('},{')]
    # 원소 개수만큼 오름차순 -> 간단하게 key=len으로 해도 되는걸 알았음
    s.sort(key=lambda x : len(x))
    answer = []
    for i in s :
        for j in i :
            if int(j) not in answer :
                answer.append(int(j))
    return answer
