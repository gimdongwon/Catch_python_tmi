# 기존 풀이 방법 (효율성 1, 2, 3 통과 못했음)
from bisect import bisect_left, bisect_right

def solution(words, queries) :
    result = []
    for query in queries :
        if query[0] == '?' and query[-1] == '?' :
            left_q = 0
            right_q = len(query)
        else :
            if query[-1] == '?' :
                lists = [0 if i != '?' else 1 for i in query]
            elif query[0] == '?' :
                lists = [2 if i != '?' else 1 for i in query]
            left_q = bisect_left(lists, 1)
            right_q = bisect_right(lists, 1)
        count = 0
        for word in words :
            if len(query) == len(word) : 
                if left_q == 0 and right_q == len(query) :
                    count += 1
                elif left_q == 0 and word[right_q:] == query[right_q:]:
                    count+= 1
                elif right_q == len(query) and word[:left_q] == query[:left_q] :
                    count+= 1
        result.append(count)
    return result

print(solution(['frodo','front','frost','frozen','frame','kakao'],['fro??','????o','fr???','fro???','pro?']))