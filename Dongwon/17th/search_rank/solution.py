# 정확성 풀이

def solution(info, querys):
    result = []
    candidates = []
    for item in info:
        condition = item.split(" ")
        candidate = {
            "language": condition[0],
            "job": condition[1],
            "level": condition[2],
            "food": condition[3],
            "score": int(condition[4])
        }
        candidates.append(candidate)
    candidates.sort(key=lambda candidate: (candidate["score"]))
    for query in querys:
        people = 0
        query = query.split(" ")
        for candidate in candidates:
            if candidate["score"] >= int(query[7]):
                if candidate["language"] == query[0] or query[0] == "-":
                    if candidate["job"] == query[2] or query[2] == "-":
                        if candidate["level"] == query[4] or query[4] == "-":
                            if candidate["food"] == query[6] or query[6] == "-":
                                people += 1
        result.append(people)
    return result


# 효율성 풀이

from bisect import bisect_left
from itertools import combinations

# str 나열로 정리
def make_all_cases(query):
    cases = []
    # 정보 항목이 5개
    for k in range(5):
        # 점수 제외 항목 4개
        for li in combinations([0, 1, 2, 3], k):
            case = ''
            for idx in range(4):
                if idx not in li:
                    case += query[idx]
                # 빈 항목은 '-' 처리
                else:
                    case += '-'
            cases.append(case)
    return cases

def solution(info, query):
    answer = []
    all_people = {}
    for i in info:
        seperate_info = i.split()
        cases = make_all_cases(seperate_info)
        # 점수 붙이기
        for case in cases:
            if case not in all_people.keys():
                all_people[case] = [int(seperate_info[4])]
            else:
                all_people[case].append(int(seperate_info[4]))
    print(all_people)
    
    # key를 기준으로 정렬
    for key in all_people.keys():
        all_people[key].sort()
    
    # 정렬한 테이블에서 이분탐색으로 찾기
    for q in query:
        seperate_q = q.split()
        target = seperate_q[0] + seperate_q[2] + seperate_q[4] + seperate_q[6]
        if target in all_people.keys():
            answer.append(len(all_people[target]) - bisect_left(all_people[target], int(seperate_q[7]), lo=0, hi=len(all_people[target])))
        else:
            answer.append(0)
    return answer