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

# Counter를 이용한 풀이 (더 효율적)
from collections import Counter
from itertools import chain

def solution(s):
    s = s.replace("{", "[")
    s = s.replace("}", "]")
    s = eval(s)
    s = list(chain(*s))
    s_counter = Counter(s)
    
    return [x[0] for x in s_counter.most_common()]