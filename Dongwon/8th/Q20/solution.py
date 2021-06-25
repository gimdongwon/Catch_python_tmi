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
    num = 0
    for i in u:
        if i == "(":
            num += 1
        else:
            if num == 0:
                return False
            num -= 1
    return True

def solution(p):
    # 1
    if len(p)==0:
        return ""
    # 2
    u,v = divide_str(p)
    # 3
    if balance_check(u):
        # 3-1
        return u + solution(v)
    else:
        # 4-1
        answer = "("
        # 4-2
        answer += solution(v)
        # 4-3
        answer += ")"
        
        # 4-4
        for i in u[1:-1]:
            if i == "(":
                answer += ")"
            else:
                answer += "("
        # 4-5
        return answer