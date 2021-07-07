# --- 프로그래머스 스타일 ---

from collections import Counter

def solution(N, stages):
    s_counter = Counter(stages)
    s_len = len(stages)
    failures = []
    
    for i in range(1, N + 1):
        try:
            failure = s_counter[i] / s_len
            s_len -= s_counter[i]
        except ZeroDivisionError:
            failure = 0
            
        failures.append(failure)
    
    return [i for i, _ in sorted(enumerate(failures, 1), key=lambda x: x[1], reverse=True)]