def divide_str(p):
    num = 0
    for i in range(len(p)):
        if p[i] == "(":
            num += 1
        else:
            num -= 1
        if num == 0:
            return p[:i+1], p[i+1:]

def balance_check(u):
    stack = []
    for i in u:
        if i == "(":
            stack.append(i)
        else:
            if len(stack) == 0:
                return False
            stack.pop()
    return True

def solution(p):
    if len(p)==0:
        return ""
    u,v = divide_str(p)
    if balance_check(u):
        return u + solution(v)
    else:
        answer = "("
        answer += solution(v)
        answer += ")"
        
        for i in u[1:-1]:
            if i == "(":
                answer += ")"
            else:
                answer += "("
        return answer