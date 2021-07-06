from itertools import permutations as pm

def elementary_arithmetic(seq:str) -> list :
    sign = []
    seq = list(map(int, seq.split()))
    for ind, num in enumerate(seq) :
        for _ in range(num) :
            if ind == 0 :
                sign.append('+')
            elif ind == 1 :
                sign.append('-')
            elif ind == 2 :
                sign.append('*')
            else :
                sign.append('//')
    return sign

def calculate(value :int, element :int, sign : str) :
    if sign == '+' :
        return value + element
    elif sign == '-' :
        return value - element
    elif sign == '*' :
        return value * element
    elif sign == "//" :
        if value < 0 :
            return abs(value) // element * -1
        else :
            return value // element
    

def solution(n:int, seq:str, sign_num:str) -> list :
    number = list(map(int, seq.split()))
    sign_list = elementary_arithmetic(sign_num)
    sign_pm = pm(sign_list, len(sign_list))
    number_list = number[1:]
    whole_value = []
    for lists in sign_pm :
        val = number[0]
        for ind in range(0, n-1) :
            val = calculate(val, number_list[ind], lists[ind])
        whole_value.append(val)
    answer = [max(whole_value), min(whole_value)]
    return answer

print(solution(2, '5 6', '0 0 1 0'))
print(solution(3, '3 4 5', '1 0 1 0'))
print(solution(6, '1 2 3 4 5 6', '2 1 1 1'))
