from collections import deque

def bracket(s) :
    stack = []
    for i in s :
        if i == '[' or i == '(' or i == '{' :
            stack.append(i)
        else :
            if not stack :
                return False
            else :
                x = stack.pop()
                if x == '(' and not i == ')' :
                    return False
                if x == '{' and not i == '}' :
                    return False
                if x == '[' and not i == ']' :
                    return False
    return True
                
def solution(s):
    if len(s) % 2 != 0 :
        return 0
    q = deque(s)
    answer = 0
    for i in range(len(s)) :
        q.rotate(-1)
        if bracket(q) :
            answer += 1
    return answer