def solution(s):
    s = s.replace("{", "[")
    s = s.replace("}", "]")
    s = eval(s)
    s.sort(key=len)
    
    result = []
    
    for x in s:
        added = [y for y in x if y not in result]
        result.extend(added)
    
    return result