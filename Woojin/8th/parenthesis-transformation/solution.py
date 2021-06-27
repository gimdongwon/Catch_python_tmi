def separate_p(p):
    if len(p) <= 2:
        return p, ""
    
    for i in range(2, len(p) + 1, 2):
        test = p[:i]
        
        if test.count("(") == test.count(")"):
            return p[:i], p[i:]

def is_correct(p):
    if len(p) == 0 or p[-1] == "(":
        return False
    
    count = 0
    
    for x in p:
        if x == "(":
            count += 1
        else:
            count -= 1
            
        if count < 0:
            return False

    return count == 0

def transform_p(u, v):
    result = "(" + solution(v) + ")"
    
    for x in u[1:-1]:
        if x == "(":
            result += ")"
        else:
            result += "("
            
    return result

def solution(p):
    if len(p) == 0:
        return ""
    
    result = ""
    u, v = separate_p(p)
    
    if is_correct(u):
        result += u
        result += solution(v)
    else:
        result += transform_p(u, v)
    
    return result