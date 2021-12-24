from collections import Counter

def solution(a):
    if len(a) == 1:
        return 0
    answer = -1
    counter = Counter(a)
    
    for k in counter.keys():
        if counter[k] <= answer:
            continue
        idx = 0
        result = 0
        while idx < len(a)-1:
            if (a[idx] != k and a[idx+1] != k) or a[idx] == a[idx+1]:
                idx += 1
                continue
            result += 1
            idx += 2
        answer = max(result, answer)
    
    if answer == -1:
        return 0
    else:
        return answer * 2
            