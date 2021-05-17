from copy import deepcopy
from itertools import permutations
from re import split

def solution(expression):
    exp_splited = split("(\+|-|\*)", expression)
    operators = ["+", "-", "*"]
    
    operators = [oper for oper in operators if oper in exp_splited]
    answer = []
    
    for permutation in permutations(operators):
        exp_splited_copy = deepcopy(exp_splited)
        
        for operator in permutation:
            while operator in exp_splited_copy:
                idx = exp_splited_copy.index(operator)
                exp_splited_copy[idx - 1:idx + 2] = [str(eval("".join(exp_splited_copy[idx - 1:idx + 2])))]
                                
        answer.append(abs(int(exp_splited_copy[0])))
        
    return max(answer)