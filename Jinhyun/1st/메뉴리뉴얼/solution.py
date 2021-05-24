from collections import Counter
from itertools import combinations

def solution(orders, course):
    answer = []
    for i in course :
        counter = Counter()
        for j in orders :
            # course에 따른 조합 list
            combi = [''.join(sorted(i)) for i in combinations(j, i)]
            counter.update(combi)
        if len(counter) == 0 :
            continue
        else :
            max_val = max(list(counter.values()))
            # 1 이하일 경우 pass
            if max_val <= 1 :
                break
            # 최댓값 원소들만 answer에 추가
            for key in counter.keys() :
                if counter[key] == max_val :
                    answer.append(key)
    return sorted(answer)
