def solution(s):
    result = []
    arr = s[2:-2].split("},{")
    arr.sort(key=len)
    for item in arr:
        target = list(map(int, item.split(",")))
        for jtem in target:
            if jtem not in result:
                result.append(jtem)
                
    return result