from itertools import permutations as pm
from copy import deepcopy

def fx_exp(expression):
    # string list를 숫자와 식 list로 변환
    frc = ['+', '-', '*']
    list_exp = []
    list_frc = []
    count = 0
    for i in expression :
        if i in frc :
            list_exp.append(count)
            list_frc.append(i)
            count = 0
        else :
            count *= 10
            count += int(i)
    list_exp.append(count)
    # 기호와 숫자 따로 반환
    return list_exp, list_frc

def frc_cal(a, b, sign) :
    #계산기
    if sign == '-' :
        return a - b
    elif sign == '+' :
        return a + b
    elif sign == '*' :
        return a * b

def solution(expression):
    frc = ['+', '-', '*']
    exp_list, frc_list = fx_exp(expression) # list 만들어주기
    pm_frc = list(pm(set(frc_list))) # 순열을 통해서 계산 순서 리스트 작성
    answer = []
    for i in pm_frc :
        # 얕은 복사가 아닌 깊은 복사를 통해 기존의 list 변하지 않도록 만들어줌
        exp_lists = deepcopy(exp_list)
        frc_lists = deepcopy(frc_list)
        for j in i :
            frc_index = []
            for index, k in enumerate(frc_lists) :
                if j == k :
                    # 무조건 기호list보다는 숫자list가 더 길기 때문에 가능한 방법
                    # 계산 결과를 기호index 다음의 숫자list원소로 넣어놓는 방법
                    x = frc_cal(exp_lists[index], exp_lists[index + 1], k)
                    frc_index.append(index)
                    exp_lists[index + 1] = x
            # reverse 하는 이유는 앞에서부터 하면 indexerror가 나기 때문에 뒤에서 부터 진행
            frc_index.sort(reverse=True)
            # 이미 계산된 값들은 기호index 다음에 위치하기 때문에 index별로 제거
            for l in frc_index :
                del frc_lists[l]
                del exp_lists[l]
        # 이미 계산된 list중 절댓값이 가장 큰 값만 answer로 넣어줬음
        answer.append(max([abs(i) for i in exp_lists]))
    return max(answer)
