from copy import deepcopy
from itertools import permutations

def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0

def get_answer(sequence, operator):
    sequence_copy = deepcopy(sequence)
    
    for oper in operator:
        if oper == "/":
            x = sequence_copy[0]
            y = sequence_copy[1]
            sequence_copy[:2] = [(sign(x)*sign(y)) * (abs(x)//abs(y))]
        else:
            x = str(sequence_copy[0])
            y = str(sequence_copy[1])
            sequence_copy[:2] = [eval(x + oper + y)]
    
    return sequence_copy[0]
    
def solution(sequence, operator_info):
    base_operator = operator_info[0] * "+" + operator_info[1] * "-" + operator_info[2] * "*" + operator_info[3] * "/"
    result = []
    
    for operator in set(permutations(base_operator, len(base_operator))):
        result.append(get_answer(sequence, operator))
    
    result.sort()
    
    return [result[-1], result[0]]
    
print(solution([5, 6], [0, 0, 1, 0])) # [30, 30]
print(solution([3, 4, 5], [1, 0, 1, 0])) # [35, 17]
print(solution([1, 2, 3, 4, 5, 6], [2, 1, 1, 1])) # [54, -24]