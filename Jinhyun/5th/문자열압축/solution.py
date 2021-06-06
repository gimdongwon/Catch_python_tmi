# -*- coding: utf-8 -*-

from collections import defaultdict

def slice_list(s, n) :
    # list를 얼마의 길이로 나눌지에 대한 코드입니다.
    i = 0
    slice_list = []
    while i + n <= len(s) :
        slice_list.append(s[i:i+n])
        i+=n
    slice_list.append(s[i:i+n])
    return slice_list

def element_list(s) :
    # 앞 원소를 기준으로 들어있으면 +1하고 들어있지 않다면 dict를 초기화해서 다시 받아오는 코드입니다.
    # ex : abcabcdede면 slice_list를 통해서 ['abc', 'abc', 'ded', 'e']를 받아오고
    #      abc : 0을 defaultdict에 넣고 abc가 있기 때문에 abc : 2 까지 만든 후
    #      '2', 'abc'를 lists에 넣은 후 defaultdict를 초기화 해주도록 코드 작성했습니다.
    lists = []
    x = defaultdict(int)
    x[s[0]] = 0
    for index, ele in enumerate(s) :
        if ele not in x.keys() :
            if x[s[index-1]] == 1 :
                pass
            else :
                lists.append(str(x[s[index-1]]))
            lists.append(s[index-1])
            x = defaultdict(int)
        x[ele] += 1
    if x[s[-1]] != 1 :
        lists.append(str(x[s[-1]]))
    lists.append(s[-1])
    return ''.join(lists)

def solution(s):
    answer_list = []
    # s의 길이의 반까지만 측정
    for i in range(1, len(s) // 2 + 1) :
        slice_lists = slice_list(s, i)
        answer_list.append(element_list(slice_lists))
    # 구분이 안될 경우 대비 기본 string도 넣어줬습니다.
    answer_list.append(s)
    answer = min(answer_list, key = lambda x : len(x))
    return len(answer)

print(solution('xababcdcdababcdcd'))
print(solution('abcabcdede'))