from collections import defaultdict # 유사 dict이며 초기값을 객체의 기본값으로 지정가능하다.
from bisect import bisect_left, bisect_right

def count_by_lange(lst, start, end):
    # print("@@ ",bisect_right(lst, end), bisect_left(lst, start))
    return bisect_right(lst, end) - bisect_left(lst, start)

def solution(words, queries):
    answer = []
    candiates = defaultdict(list) 
    reverse_candiates = defaultdict(list) 
    
    for word in words:
        candiates[len(word)].append(word)
        reverse_candiates[len(word)].append(word[::-1]) # 문자열 뒤집기
    
    for candiate in candiates.values():
        candiate.sort()
    for candiate in reverse_candiates.values():
        candiate.sort()
    
    for query in queries:
        # print(query)
        if query[0] == "?":
            lst = reverse_candiates[len(query)]
            start, end = query[::-1].replace("?", "a"), query[::-1].replace("?", "z")
        else:
            lst = candiates[len(query)]
            start, end = query.replace("?", "a"), query.replace("?", "z")
        # print(lst, start, end)
        answer.append(count_by_lange(lst, start, end))
        # print(answer)
    return answer
    